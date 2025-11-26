# mapper/cli.py

import argparse

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="AWS Cloud Mapper - network visualization tool"
    )

    region_group = parser.add_mutually_exclusive_group(required=False)
    region_group.add_argument(
        "--region",
        help="Single AWS region to map, e.g. ap-south-1",
    )
    region_group.add_argument(
        "--all-regions",
        action="store_true",
        help="Map all account-enabled regions",
    )

    parser.add_argument(
        "--profile",
        help="AWS named profile to use (fallback: environment/default profile)",
    )

    parser.add_argument(
        "--out",
        default="cloud_map.dot",
        help="Output DOT filename (default: cloud_map.dot)",
    )

    return parser


def parse_args():
    parser = build_parser()
    return parser.parse_args()
