import argparse

def build_arg_parser():

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
    parser = build_arg_parser()
    return parser.parse_args()