import boto3
from botocore.config import Config


def boto3_session():
    return boto3.session.Session

def ec2_session_client(region: str):
    return boto3.client('ec2',region_name=region,config=Config(retries={"max_attempts": 10}))

def elb_session(region: str):
    session = boto3_session()
    elb2 = session.client("elbv2", region_name=region, config=Config(retries={"max_attempts": 10}))
    
def ec2_session_resource(region: str):
    session = boto3_session()
    ec2_res = session.resource("ec2", region_name=region, config=Config(retries={"max_attempts": 10}))

