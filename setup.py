from setuptools import setup, find_packages

setup(
    name="aws-cloud-mapper",
    version="0.1.0",
    description="AWS Cloud Mapper - Network visualization tool",
    author="boopesh-foxy",
    email="contact.boopesh@gmail.com",
    packages=find_packages(),
    install_requires=[
        "boto3>=1.28.0",
        "botocore>=1.31.0",
    ],
    entry_points={
        "console_scripts": [
            "cloud-mapper=mapper.main:main",
        ],
    },
    python_requires=">=3.11",
)
