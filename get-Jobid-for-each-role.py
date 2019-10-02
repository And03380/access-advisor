import sys
import boto3

client = boto3.client('iam')

f2= open("Role_ARN.txt")
Job_Ids_from_file = f2.read().split("\n")
f2.close()

f3= open("JobId_list.txt","w+")

for role in Job_Ids_from_file:
    string_role = str(role)
    print("stringROLLLLL:    " + string_role)
    response = client.generate_service_last_accessed_details(
    Arn=string_role
)
    
    ##print(response['JobId'])
    f3.write(response['JobId'] + "\n")
