import boto3

iam = boto3.resource('iam')

role_list = iam.list_roles()
for role in role_list:
    print(role)
