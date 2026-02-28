# AWS Cloud Mapper

AWS Cloud Mapper is a read-only network visualization tool that discovers resources in your AWS account and generates a Graphviz DOT file representing connectivity between VPCs, subnets, route tables, gateways, load balancers, ENIs, instances, and security groups.

You can then render this DOT file into PNG, SVG, or PDF using Graphviz to understand your AWS network topology at a glance.

---

## Features

- Read-only AWS inspection (no write or modify operations).
- Supports:
  - VPCs and CIDR blocks
  - Subnets and AZ placement
  - Route tables and their associations
  - Internet Gateways (IGW)
  - NAT Gateways (NATGW)
  - VPC Endpoints
  - VPC Peering connections
  - VPN Gateways (VGW)
  - Elastic Network Interfaces (ENI)
  - EC2 instances and their ENIs
  - Security Groups and their ingress rules (SG → SG and SG → CIDR)
  - Application Load Balancers (ALB)
  - Network Load Balancers (NLB)
  - Target Groups and their targets (instances or IPs)
- Single region or all enabled regions.
- Outputs a single Graphviz DOT file that can be rendered with `dot`.

---

## AWS permissions

This tool only uses read-only Describe/List APIs. A minimal IAM policy should include permissions like:

```text
ec2:DescribeRegions

ec2:DescribeVpcs

ec2:DescribeSubnets

ec2:DescribeRouteTables

ec2:DescribeInternetGateways

ec2:DescribeNatGateways

ec2:DescribeVpnGateways

ec2:DescribeVpcEndpoints

ec2:DescribeVpcPeeringConnections

ec2:DescribeSecurityGroups

ec2:DescribeNetworkInterfaces

ec2:DescribeInstances

elasticloadbalancing:DescribeLoadBalancers

elasticloadbalancing:DescribeTargetGroups

elasticloadbalancing:DescribeTargetHealth

```


---

## Docker Usage

This project includes a Dockerfile for containerized visualization rendering and serving.

### Prerequisites
- Docker installed on your system
- A generated `graph.dot` file in the project root

### Building and Running

The Dockerfile uses a multi-stage build process:

1. **Builder stage**: Converts the DOT file to SVG using Graphviz
2. **Runtime stage**: Serves the SVG visualization via nginx

```bash
# Build the Docker image
docker build -t aws-cloud-mapper .

# Run the container
docker run -p 8080:80 aws-cloud-mapper
