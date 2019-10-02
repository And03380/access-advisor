import sys
import boto3
iam = boto3.client('iam')
marker = None

role_list = iam.list_roles()

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
            
    try:
        marker = page['Marker']
        print(marker)
    except KeyError:
        sys.exit()
        
for roley in role_list:
    print(roley)
