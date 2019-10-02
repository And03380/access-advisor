import sys
import boto3

client = boto3.client('iam')

f2 = ["arn:aws:iam::439463768147:role/flowlogsRole", "arn:aws:iam::439463768147:role/LambdaGuardrail-EC2"]

fruits = ["apple", "banana", "cherry"]
for roles in f2:
    
    response = client.generate_service_last_accessed_details(
    Arn=roles
)

print(response)


