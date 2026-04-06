# AWS Cloud Mapper

AWS Cloud Mapper is a read-only CLI tool that discovers networking resources in your AWS account and generates a [Graphviz](https://graphviz.org/) DOT file representing the connectivity between them. The DOT file can be rendered into PNG, SVG, or PDF to visualize your AWS network topology.

---

## Architecture

```
CLI args (argparse)
      │
      ▼
  main.py              ← entry point, orchestrates the pipeline
      │
      ├── cli.py       ← argument parsing (--region, --all-regions, --out, --debug)
      ├── logger.py    ← centralized logging setup (RotatingFileHandler + StreamHandler)
      │
      ▼
cloud_mapper_fetch.py  ← AWS API calls via boto3, returns raw resource data
      │
      ▼
cloud_mapper_init.py   ← data_fetch_aws class, organizes resources into typed dicts
      │
      ▼
generate_dot_files()   ← writes Graphviz DOT file from structured resource data
      │
      ▼
  output.dot           ← rendered with `dot` or served via Docker + nginx
```

---

## Module breakdown

### `mapper/main.py`
Entry point. Parses CLI args, calls `setup_logging()`, then routes to either single-region or all-regions fetch. Calls `generate_dot_files()` with the collected data and output path.

### `mapper/cli.py`
Wraps Python's `argparse`. Defines a mutually exclusive group for `--region` and `--all-regions` so both cannot be passed simultaneously. Logs parsed args at DEBUG level via `vars(args)` which converts the `Namespace` object to a readable dict.

### `mapper/logger.py`
Centralized logging configuration. `setup_logging()` attaches two handlers to the root logger:
- `RotatingFileHandler` — writes to `~/.cloud-mapper/cloud-mapper.log`, rotates at 5 MB, retains 3 backups
- `StreamHandler` — writes to stdout for interactive use

All other modules call `logging.getLogger(__name__)` and inherit this configuration through Python's logger hierarchy without needing to import `logger.py` directly.

### `mapper/boto3_resources.py`
Factory functions for boto3 clients and resources. Centralizes session creation so the rest of the codebase never instantiates boto3 directly. All clients are configured with `Config(retries={"max_attempts": 10})` to handle AWS API throttling gracefully.

- `boto3_session()` — returns a `boto3.Session`
- `ec2_session_client(region)` — returns an EC2 client
- `elb_session(region)` — returns an ELBv2 client
- `ec2_session_resource(region)` — returns an EC2 resource (higher-level ORM-style API)

### `mapper/cloud_mapper_init.py`
Defines `data_fetch_aws`, a class that holds all discovered resources as typed dicts keyed by resource ID. Each resource type has its own attribute (`vpcs`, `subnets`, `igws`, etc.). `fetch_resources(self, region)` populates these by calling the relevant AWS `describe_*` APIs.

### `mapper/cloud_mapper_fetch.py`
Thin orchestration layer. `get_regions()` calls `ec2.describe_regions(AllRegions=False)` to return only regions enabled for the account. `get_resources()` instantiates `data_fetch_aws` and triggers the fetch pipeline.

---

## AWS APIs used

All calls are read-only. No write or mutating operations are performed.

| Resource | API call |
|---|---|
| Regions | `ec2.describe_regions` |
| VPCs | `ec2.describe_vpcs` |
| Subnets | `ec2.describe_subnets` |
| Route Tables | `ec2.describe_route_tables` |
| Internet Gateways | `ec2.describe_internet_gateways` |
| NAT Gateways | `ec2.describe_nat_gateways` |
| VPC Endpoints | `ec2.describe_vpc_endpoints` |
| VPC Peering | `ec2.describe_vpc_peering_connections` |
| VPN Gateways | `ec2.describe_vpn_gateways` |
| ENIs | `ec2.describe_network_interfaces` |
| EC2 Instances | `ec2.describe_instances` |
| Security Groups | `ec2.describe_security_groups` |
| ALB / NLB | `elbv2.describe_load_balancers` |
| Target Groups | `elbv2.describe_target_groups` |

---

## DOT file output

The output is a Graphviz directed graph (`digraph`). Resources are nodes, relationships are directed edges. Regions and VPCs are rendered as `subgraph cluster_*` blocks which draw a bounding box around their members.

Node shapes convey resource type:
- `diamond` — Internet Gateway
- `box3d` — EC2 instance
- `folder` — Security Group
- `component` — VPC Peering
- `oval` — CIDR block

---

## Logging

Logs are written to `~/.cloud-mapper/cloud-mapper.log` with rotation at 5 MB, keeping 3 backups. Simultaneous console output is enabled by default. Pass `--debug` to include DEBUG-level messages.

Log format: `%(asctime)s [%(levelname)s] %(name)s - %(message)s`

---

## Docker

A multi-stage Dockerfile is included for rendering and serving the visualization:

- Stage 1 (`builder`) — Alpine + Graphviz, converts `graph.dot` to SVG
- Stage 2 — nginx Alpine, serves the SVG at port 80

The final image contains only nginx and the rendered SVG. Graphviz is not present in the runtime image, keeping it minimal.

---

## Dev Container

A `.devcontainer/` configuration is included for VS Code. It provisions:
- Python 3.11
- AWS CLI
- ms-python extension
- Mounts `~/.aws` credentials from the host into the container
- Runs `pip install -r requirements.txt` on container start
- Forwards port 8080 for the nginx visualization server

---

## Required IAM permissions

```json
{
  "Effect": "Allow",
  "Action": [
    "ec2:DescribeRegions",
    "ec2:DescribeVpcs",
    "ec2:DescribeSubnets",
    "ec2:DescribeRouteTables",
    "ec2:DescribeInternetGateways",
    "ec2:DescribeNatGateways",
    "ec2:DescribeVpcEndpoints",
    "ec2:DescribeVpcPeeringConnections",
    "ec2:DescribeVpnGateways",
    "ec2:DescribeNetworkInterfaces",
    "ec2:DescribeInstances",
    "ec2:DescribeSecurityGroups",
    "elasticloadbalancing:DescribeLoadBalancers",
    "elasticloadbalancing:DescribeTargetGroups",
    "elasticloadbalancing:DescribeTargetHealth"
  ],
  "Resource": "*"
}
```
