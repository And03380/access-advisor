import sys
import boto3

client = boto3.client('iam')

response = client.generate_service_last_accessed_details(
    Arn='arn:aws:iam::439463768147:role/EKS-Managment'
)

print(response)
