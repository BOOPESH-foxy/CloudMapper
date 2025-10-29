import boto3

def boto3_ec2_resource(region: str):
    return boto3.resource('ec2',region)