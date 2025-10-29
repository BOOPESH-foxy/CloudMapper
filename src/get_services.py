import boto3
import boto3_resources
from botocore.exceptions import ClientError
from typing import Any

def fetch_resources():
    pass

class data_init:

    def __init__(self):

        self.albs: dict[str, dict[str, Any]] = {}
        self.vpcs: dict[str, dict[str, Any]] = {}
        self.subnets: dict[str, dict[str, Any]] = {}
        self.route_tables: dict[str, dict[str, Any]] = {}
        self.igws: dict[str, dict[str, Any]] = {}
        self.nat_gws: dict[str, dict[str, Any]] = {}
        self.vpc_endpoints: dict[str, dict[str, Any]] = {}
        self.peering: dict[str, dict[str, Any]] = {}
        self.vgws: dict[str, dict[str, Any]] = {}
        self.sg: dict[str, dict[str, Any]] = {}
        self.enis: dict[str, dict[str, Any]] = {}
        self.instances: dict[str, dict[str, Any]] = {}
        self.albs: dict[str, dict[str, Any]] = {}
        self.nlbs: dict[str, dict[str, Any]] = {}
        self.target_groups: dict[str, dict[str, Any]] = {}
