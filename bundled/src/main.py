import typer
from tqdm import tqdm
import cloud_mapper_fetch

app = typer.Typer(help="Cloud mapper - visualize the network flow on resources on the configured aws profile and region")

@app.command("init")
def typer_init():
    "Gets all the resources on the provided aws profile and region"
    cloud_mapper_fetch.get_resources()


if __name__ == "__main__":
    app()