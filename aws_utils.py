import boto3
import os


LOCALSTACK_ENDPOINT = os.getenv('LOCALSTACK_ENDPOINT')

def initialize_s3_clients():
    # Check if the environment variable 'ENVIRONMENT' is set to 'local'
    if os.environ.get('ENVIRONMENT') == 'local':
        # Use the custom endpoint URL for localstack
        s3 = boto3.client('s3', endpoint_url=LOCALSTACK_ENDPOINT)
        print('Initialized S3 client for local environment')
    else:
        s3 = boto3.client('s3')
        print('Initialized S3 client for AWS environment')

    return s3

def get_sqs_client():
    if os.environ.get('ENVIRONMENT') == 'local':
        sqs = boto3.client('sqs', endpoint_url=LOCALSTACK_ENDPOINT)
        sqs_resource = boto3.resource('sqs', endpoint_url=LOCALSTACK_ENDPOINT)
        print('Initialized SQS client and resource for local environment')
    else:
        sqs = boto3.client('sqs')
        sqs_resource = boto3.resource('sqs')
        print('Initialized SQS client and resource for AWS environment')
    return sqs, sqs_resource
