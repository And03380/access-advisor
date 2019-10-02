import boto3

client = boto3.client('iam')

role_list = client.list_roles()

for role in role_list[]:
    print(role)
