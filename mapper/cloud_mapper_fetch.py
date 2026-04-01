import boto3
import argparse
import logging
from boto3_resources import ec2_session_client
from typing import Any

logger = logging.getLogger(__name__)

def get_resources():
    pass

def get_regions(region = "us-east-1"):
    """
    Get a list of all enabled AWS regions for the account.
    Note:
        AllRegions=False means only enabled regions are returned.
    """
    session = ec2_session_client(region)
    result_describe_regions = session.describe_regions(AllRegions = False)
    regions_list = []
    
    for r in result_describe_regions["Regions"]:
        regions_list.append(r["RegionName"])
    logger.warning("Getting all regions")

    return regions_list
