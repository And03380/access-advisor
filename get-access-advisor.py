import sys
import boto3
import json
import requests
from pathlib import Path
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
        print("Next Page : {} ".format(page['IsTruncated']))
        u = page['Roles']
        for user in u:
            print(user['Arn'])
            f.write(user['Arn'])
    try:
            marker = page['Marker']
            print(marker)
    except KeyError:
            sys.exit()
