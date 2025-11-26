import boto3
import argparse
from boto3_resources import ec2_session_client
from typing import Any

def get_resources():
    pass

def get_regions(region):

    session = ec2_session_client(region)
    result_describe_regions = session.describe_regions(AllRegions = False)
    regions_list = {}
    
    for r in result_describe_regions["Regions"]:
        regions_list.append(r["RegionName"])

    print(regions_list)


def resolve_regions(region):

    ap = argparse.ArgumentParser(description="AWS Cloud Mapper to Graphviz DOT")
    ap.add_argument("--region", help="Single AWS region to map, e.g., ap-south-1")
    ap.add_argument("--all-regions", action="store_true", help="Map all enabled regions")
    ap.add_argument("--profile", help="AWS named profile")
    ap.add_argument("--out", default="cloud_map.dot", help="Output DOT file path")
    args = ap.parse_args()

    if(args.region):
        return get_regions(args.region)
    else:
        return get_regions()


resolve_regions()