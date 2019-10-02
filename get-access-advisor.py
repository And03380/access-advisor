import boto3

iam = boto3.resource('iam')
role = iam.Role('name')

list_roles(
    PathPrefix='string',
    Marker='string',
    MaxItems=123
)
