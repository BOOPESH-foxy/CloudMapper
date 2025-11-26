import boto3
import boto3_resources
from botocore.exceptions import ClientError
from typing import Any

class data_fetch_aws:

    def __init__(self):

        self.albs: dict[str, Any] = {}
        self.vpcs: dict[str, Any] = {}
        self.subnets: dict[str, Any] = {}
        self.route_tables: dict[str, Any] = {}
        self.igws: dict[str, Any] = {}
        self.nat_gws: dict[str, Any] = {}
        self.vpc_endpoints: dict[str, Any] = {}
        self.peering: dict[str, Any] = {}
        self.vgws: dict[str, Any] = {}
        self.sg: dict[str, Any] = {}
        self.enis: dict[str, Any] = {}
        self.instances: dict[str, Any] = {}
        self.albs: dict[str, Any] = {}
        self.nlbs: dict[str, Any] = {}
        self.target_groups: dict[str, Any] = {}


    def fetch_resources():
        pass