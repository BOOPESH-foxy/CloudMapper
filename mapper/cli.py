import argparse
import logging
logger = logging.getLogger(__name__)

def build_arg_parser():
    """
    Build and configure the command-line argument parser.
    
    Defines three arguments:
    - --region: Specify a single AWS region to map
    - --all-regions: Map all enabled regions in the account (mutually exclusive with --region)
    - --out: Specify the output DOT file name (default: resource_map.dot)
    
    Returns:
        argparse.ArgumentParser: Configured argument parser
    """
    parser = argparse.ArgumentParser(description = "AWS Cloud Mapper - A network visualization tool by boo-foxy")
    region_group = parser.add_mutually_exclusive_group(required=False)

    region_group.add_argument("--region",
                            help="A single region to map resources")

    region_group.add_argument("--all-regions",
                            action="store_true",
                            help="Map all regions allowed on the provided account")

    parser.add_argument("--out",
                        default="resource_map.dot",
                        help="Name of the output dot file")
    return parser

def parse_args():
    """ Parse command-line arguments provided by the user. """
    parser = build_arg_parser()
    args = parser.parse_args()
    logger.info(f"Parsed args: {vars(args)}")
    return args