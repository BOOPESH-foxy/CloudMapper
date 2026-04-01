"""Cloud mapper - visualize the network flow of resources on the configured aws profile and region"""

import cli
from logger import setup_logging
import logging
from cloud_mapper_fetch import get_regions

setup_logging()
logger = logging.getLogger(__name__)

def main():
    args = cli.parse_args()
    if(args.region):
        region_data = fetch_resources( args.region )
        logger.info(f"Fetching resources from {args.region}")
    elif(args.all_regions):
        regions_list = determine_regions()
        logger.info(f"Fetching resources from {regions_list}")

    output_file = args.out
    # generate_dot_files( region_data, output_file )

def determine_regions():
    regions_list = get_regions()
    return regions_list

def fetch_resources(region):
    """Fetch all AWS resources from the specified regions."""
    pass

def generate_dot_files(region_data,output_file):
    """Generate a Graphviz DOT file from the fetched AWS resources."""
    pass

if __name__ == "__main__":
    main()