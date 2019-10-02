import sys
import boto3

client = boto3.client('iam')

f2= open("Results.csv","w+")
f2 = ["arn:aws:iam::439463768147:role/flowlogsRole", "arn:aws:iam::439463768147:role/LambdaGuardrail-EC2", "arn:aws:iam::439463768147:role/RedlockReadOnlyRole",
     "arn:aws:iam::439463768147:role/S3ReadOnlyEC2Access"]

for roles in f2:
    
    response = client.generate_service_last_accessed_details(Arn=roles)
    print(response['JobId'])
    print(1)



