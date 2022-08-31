import boto3
import time
import os
from os.path import join, dirname
from dotenv import load_dotenv

import upload
import filename_generator

# Load environment variables
load_dotenv()

# Create SQS client
queue_url = os.getenv("QUEUE_URL")
sqs = boto3.client('sqs', 
                    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"), 
                    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"), 
                    region_name=os.getenv("AWS_DEFAULT_REGION"),
                    endpoint_url=queue_url)

while(True):
    # Receive message from SQS queue
    response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=[
            'SentTimestamp'
        ],
        MaxNumberOfMessages=1,
        MessageAttributeNames=[
            'All'
        ],
        VisibilityTimeout=0,
        WaitTimeSeconds=0
    )

    print(response)

    if 'Messages' in response:
        message = response['Messages'][0]
        receipt_handle = message['ReceiptHandle']

        filename = filename_generator.generate()
        response = upload.put_object(filename, "hello world!")

        if response == 200:
            # Delete received message from queue
            sqs.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=receipt_handle
            )
            print('Received and deleted message: %s' % message["Body"])
        else:
            print('Will try again')
    time.sleep(3)