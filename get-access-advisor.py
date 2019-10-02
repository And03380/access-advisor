import boto3

iam = boto3.client('iam')

role_list = iam.list_roles()

paginator = iam.get_paginator('list_roles')
for response in paginator.paginate():
    print(response.arn)
