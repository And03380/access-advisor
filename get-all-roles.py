import sys
import boto3

iam = boto3.client('iam')
marker = None

role_list = iam.list_roles()
full_role_list = []
f= open("Role_ARN.txt","w+")


while True:
    paginator = iam.get_paginator('list_roles')
    response_iterator = paginator.paginate( 
        PaginationConfig={
            'StartingToken': marker})
    for page in response_iterator:
        u = page['Roles']
        for user in u[0]:
            print(user['Arn'])
            f.write(user['Arn'] + "\n") 
    try:
            marker = page['Marker']
            print(marker)
    except KeyError:
            sys.exit()
