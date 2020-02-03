import boto3
import json
import random


client_s3 = boto3.client('s3')
client_firehouse = boto3.client('firehose')
client_ec2 = boto3.client('ec2')

def events():
    for x in range(100):
        numberList = [1,2,3,4,5]
        selector = random.choice(numberList)

        if selector == 1:
            response = client_s3.list_buckets()
            return response

        elif selector == 2:
            response = client_firehouse.list_delivery_streams()
            return response

        elif selector == 3:
            response = client_ec2.describe_instances()
            return response

        elif selector == 4:
            response = client_ec2.describe_hosts()
            return response

        elif selector == 5:
            response = client.list_buckets()
            return response

        else:
            response = client.list_queues()
            return response
events()
