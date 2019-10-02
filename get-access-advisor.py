import boto3

client = boto3.client('iam')

role_list = client.list_roles()
print role_list[2]
for role in range(len(role_list)):
    print(role)
