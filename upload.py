import boto3
import os
from dotenv import load_dotenv
import datetime

# Load environment variables
load_dotenv()

#Creating S3 Resource From the Session.
s3 = boto3.resource('s3',
                    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"), 
                    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"), 
                    region_name=os.getenv("AWS_DEFAULT_REGION"),
                    endpoint_url=os.getenv("ENDPOINT_URL"))

def put_object(filename, content):
    object = s3.Object(os.getenv("S3_BUCKET_NAME"), filename)

    result = object.put(Body=content)

    res = result.get('ResponseMetadata')

    if res.get('HTTPStatusCode') == 200:
        print('File Uploaded Successfully')
        return 200
    else:
        print('File Not Uploaded')
        return 400