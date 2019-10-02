import sys
import boto3

client = boto3.client('iam')

response = client.generate_service_last_accessed_details(
    Arn='arn:aws:iam::439463768147:role/EKS-Managment'
)

print(response)

marker = None

full_role_list = []

while True:
    paginator = iam.get_paginator('generate_service_last_accessed_details')
    response_iterator = paginator.paginate( 
        PaginationConfig={
            'StartingToken': marker})
    for page in response_iterator:
        print("Next Page : {} ".format(page['IsTruncated']))
        u = page['Roles']
        for user in u:
            print(user)
            
    try:
            marker = page['Marker']
            print(marker)
    except KeyError:
            sys.exit()
