import boto3
import json
import random


client_s3 = boto3.client('s3')
client_firehouse = boto3.client('firehose')
client_ec2 = boto3.client('ec2')
client_sqs = boto3.client('sqs')
client_kinesis = boto3.client('kinesis')
client_events = boto3.client('events')
client_sms = boto3.client('sms')


def events():
    for x in range(100):
        numberList = [1,2,3,4,5,6,7,8,9,10,11]
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
            response = client_s3.list_buckets()
            return response
        
        elif selector == 6:
            response = client_events.describe_event_bus()
            return response
        
        elif selector == 7:
            response = client_ec2.describe_ipv6_pools()
            return response
        
        elif selector == 8:
            response = client_events.describe_local_gateway_virtual_interfaces()
            return response
        
        elif selector == 9:
            response = client_kinesis.list_streams()
            return response
        
        elif selector == 10:
            response = client_sms.list_apps()
            return response
        
        elif selector == 11:
            response = client_ec2.describe_tags()
            return response

        else:
            response = client_sqs.list_queues()
            return response
events()
