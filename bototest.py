#import boto3

# Let's use Amazon S3
#s3 = boto3.resource('s3')
# Print out bucket names
#for bucket in s3.buckets.all():
#    print(bucket.name)
#cloudwatch = boto3.resource('cloudwatch')
#paginator = cloudwatch.get_paginator('describe_alarms')
#for response in paginator.paginate(Dimensions=[{'BucketName': 'Value'}],
#                                   MetricName='BucketSizeBytes',
#                                   Namespace='AWS/S3'):
#    print(response['Metrics'])
from datetime import datetime, timedelta
import boto3

seconds_in_one_day = 86400  # used for granularity

cloudwatch = boto3.client('cloudwatch',region_name='us-east-1')

response = cloudwatch.get_metric_statistics(
    Namespace='AWS/S3',
    Dimensions=[
        {
            'Name': 'BucketName',
            'Value': 'us-east-1-dev-cxengagelabs-artifacts'
        },
        {
            'Name': 'StorageType',
            'Value': 'StandardStorage'
        }
    ],
    MetricName='BucketSizeBytes',
    StartTime=datetime.now() - timedelta(days=1),
    EndTime=datetime.now(),
    Period=seconds_in_one_day,
    Statistics=[
        'Average'
    ],
    Unit='Bytes'
)

print(response)
