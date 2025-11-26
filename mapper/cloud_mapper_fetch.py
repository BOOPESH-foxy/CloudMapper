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
