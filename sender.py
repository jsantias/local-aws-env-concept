import boto3
import os
import time
from os.path import join, dirname
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create SQS client
queue_url = os.getenv("QUEUE_URL")
sqs = boto3.client('sqs',                     
                    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"), 
                    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"), 
                    region_name=os.getenv("AWS_DEFAULT_REGION"),
                    endpoint_url=queue_url)

# Send message to SQS queue
response = sqs.send_message(
    QueueUrl=queue_url,
    DelaySeconds=10,
    MessageAttributes={
        'Title': {
            'DataType': 'String',
            'StringValue': 'Blue skies, rainbows... and Skittles!'
        },
        'Author': {
            'DataType': 'String',
            'StringValue': 'John Santias'
        }
    },
    MessageBody=("Hello World!")
)

print('Message sent to %s' % queue_url) 
print(response['MessageId'])
time.sleep(10)