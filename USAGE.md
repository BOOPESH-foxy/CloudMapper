# Usage & Setup

## Prerequisites

- Python 3.11+
- AWS credentials configured (`~/.aws/credentials` or environment variables)
- Graphviz installed (only needed to render the DOT file locally)

Install Graphviz:
```bash
# Ubuntu / Debian
sudo apt install graphviz

# macOS
brew install graphviz
```

---

## Installation

Clone the repo and install as an editable package:

```bash
git clone https://github.com/boopesh-foxy/aws-cloud-mapper.git
cd aws-cloud-mapper
pip install -e .
```

The `-e` flag installs in editable mode — changes to source files take effect immediately without reinstalling.

After install, the `cloud-mapper` command is available globally in your terminal.

---

## AWS credentials

The tool uses your configured AWS credentials. Set these up with:

```bash
aws configure
```

This writes to `~/.aws/credentials` and `~/.aws/config`. boto3 picks these up automatically.

Alternatively, use environment variables:

```bash
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
export AWS_DEFAULT_REGION=us-east-1
```

---

## Running the tool

Map a single region:
```bash
cloud-mapper --region ap-south-1
```

Map all enabled regions in your account:
```bash
cloud-mapper --all-regions
```

Specify a custom output file name:
```bash
cloud-mapper --region us-east-1 --out my-network.dot
```

Enable debug logging:
```bash
cloud-mapper --region us-east-1 --debug
```

---

## Rendering the DOT file

Once you have a `.dot` file, render it with Graphviz:

```bash
# PNG
dot -Tpng resource_map.dot -o network.png

# SVG
dot -Tsvg resource_map.dot -o network.svg

# PDF
dot -Tpdf resource_map.dot -o network.pdf
```

Open the output file in any browser or image viewer.

---

## Docker usage

If you don't want to install Graphviz locally, use Docker to render and serve the visualization.

Build and run:
```bash
docker build -t aws-cloud-mapper .
docker run -p 8080:80 aws-cloud-mapper
```

Then open `http://localhost:8080` in your browser to view the SVG.

The Dockerfile expects a `graph.dot` file in the project root. Generate it first with the CLI, then rename or copy it:
```bash
cloud-mapper --region ap-south-1 --out graph.dot
docker build -t aws-cloud-mapper .
docker run -p 8080:80 aws-cloud-mapper
```

---

## Dev Container (VS Code)

Open the project in VS Code and click "Reopen in Container" when prompted. The dev container will:

1. Install Python 3.11 and AWS CLI
2. Mount your `~/.aws` credentials into the container
3. Run `pip install -r requirements.txt` automatically
4. Forward port 8080 for the nginx server

No local Python or AWS CLI installation needed.

---

## Logs

Logs are written to `~/.cloud-mapper/cloud-mapper.log`. The file rotates at 5 MB and keeps 3 backups.

Tail logs in real time:
```bash
tail -f ~/.cloud-mapper/cloud-mapper.log
```

---

## CLI reference

| Flag | Description | Default |
|---|---|---|
| `--region REGION` | Single AWS region to map | — |
| `--all-regions` | Map all enabled regions | — |
| `--out FILENAME` | Output DOT file name | `resource_map.dot` |
| `--debug` | Enable DEBUG level logging | off |

`--region` and `--all-regions` are mutually exclusive. One must be provided.
