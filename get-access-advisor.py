import boto3

iam = boto3.resource('iam')
role = iam.Role('name')

list_roles_resp = iam.list_roles()
for role in list_roles_resp[]:
    print(role)
