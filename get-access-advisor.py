import sys
import boto3
iam = boto3.client('iam')
marker = None

role_list = iam.list_roles()

while True:
    paginator = iam.get_paginator('list_users')
    response_iterator = paginator.paginate( 
        PaginationConfig={
            'PageSize': 10,
            'StartingToken': marker})
    for page in response_iterator:
        print("Next Page : {} ".format(page['IsTruncated']))
        u = page['Users']
        for user in u:
            print(user['arn'])
    try:
        marker = page['Marker']
        print(marker)
    except KeyError:
        sys.exit()
