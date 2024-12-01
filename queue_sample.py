from aws_utils import get_sqs_client


def exec_queue():
    sqs, sqs_resource = get_sqs_client()
    queue = sqs_resource.get_queue_by_name(QueueName='my-queue')
    response = queue.send_message(MessageBody='Hello World from Python!')
    print(f"-Start----------------Send-Message-To-Queue--------------------")
    print(f"{response = }")
    print(f"-End------------------Send-Message-To-Queue--------------------")


def receive_msg_from_queue():
    sqs, sqs_resource = get_sqs_client()
    queue_url = "http://sqs.us-east-1.localhost.localstack.cloud:4566/000000000000/my-queue"
    response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=['SentTimestamp'],
        MaxNumberOfMessages=1,
        MessageAttributeNames=['All'],
        VisibilityTimeout=0,
        WaitTimeSeconds=0
    )
    print(f"-Start----------------Receive-Message-From-Queue--------------------")
    print(f"{response = }")
    print(f"-End------------------Receive-Message-From-Queue--------------------")


if __name__ == '__main__':
    exec_queue()
    receive_msg_from_queue()
