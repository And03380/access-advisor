import sys
import boto3
import botocore

client = boto3.client('iam')

f2= open("Role_ARN.txt")
Job_Ids_from_file = f2.read().split("\n")
f2.close()

f3= open("JobId_list.txt","w+")

def HelperFun(x): 
    y = str(x)
    #print(y)
    response = client.generate_service_last_accessed_details(
    Arn=y
)
    #print(response['JobId'])
    f3.write(response['JobId'] + "\n")

for role in Job_Ids_from_file:
    HelperFun(role)
    #response = client.generate_service_last_accessed_details(
    #Arn="\"role\": \"" + role + "\""
#)    
    #print(response['JobId'])
    #f3.write(response['JobId'] + "\n")
