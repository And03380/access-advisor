import boto3

iam = boto3.client('iam')

role_list = iam.list_roles()

while True:
    paginator = iam.get_paginator('list_roles')
    response_iterator = paginator.paginate( 
        PaginationConfig={
            'PageSize': 10,
            'StartingToken': marker})
    for role in response_iterator:
        print("Next Page : {} ".format(role['IsTruncated']))
        u = role['Users']
        for user in u:
            print(user['UserName'])
    try:
        marker = role['Marker']
        print(marker)
    except KeyError:
        sys.exit()
