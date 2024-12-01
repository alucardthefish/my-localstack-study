import boto3
import os
import json

def initialize_s3_clients():
    localstack_endpoint = os.getenv("LOCALSTACK_ENDPOINT")
    # Check if the environment variable 'ENVIRONMENT' is set to 'local'
    if os.environ.get('ENVIRONMENT') == 'local':
        # Use the custom endpoint URL for localstack
        endpoint_url = localstack_endpoint
        s3 = boto3.client('s3', endpoint_url=endpoint_url)
        print('Initialized S3 client for local environment')
    else:
        s3 = boto3.client('s3')
        print('Initialized clients for AWS environment')

    return s3

