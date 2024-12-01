import boto3
import os
import json


def initialize_clients():
    localstack_endpoint = os.getenv("LOCALSTACK_ENDPOINT")
    # Check if the environment variable 'ENVIRONMENT' is set to 'local'
    if os.environ.get('ENVIRONMENT') == 'local':
        # Use the custom endpoint URL for localstack
        endpoint_url = localstack_endpoint
        sns = boto3.client('sns', endpoint_url=endpoint_url)
        s3 = boto3.client('s3', endpoint_url=endpoint_url)
        print('Initialized clients for local environment')
    else:
        sns = boto3.client('sns')
        s3 = boto3.client('s3')
        print('Initialized clients for AWS environment')

    return sns, s3


def lambda_handler(event, context):
    sns, s3 = initialize_clients()

    # Emit a notification to an SNS topic
    topic = sns.create_topic(Name="my-topic")
    topic_arn = topic.get('TopicArn', 'arn:aws:sns:us-east-1:000000000000:my-topic')
    message = {
        "default": json.dumps(event),
        "sms": "Here is a short version of the message",
        "email": "Here is a longer version of the message",
    }

    sns.publish(TopicArn=topic_arn, Message=json.dumps(message))
    print("Sent message to SNS topic")

    # Write an object to an S3 bucket
    bucket_name = "my-bucket"
    object_key = "my-object.txt"
    s3.put_object(Bucket=bucket_name, Key=object_key, Body=json.dumps(event))
    print("Sent message to S3 bucket")

    return f"Finished, wrote {event} to bucket {bucket_name} and sent message to topic"
