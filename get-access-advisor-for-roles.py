import sys
import boto3
import json 
import botocore
#from bson import json_uti

client = boto3.client('iam')

f2= open("JobId_list.txt")
Job_Ids_from_file = f2.read().split("\n")
f2.close()

f3= open("out_puts.txt","w+")

def HelperFun(x): 
    y = str(x)
    #print(y)
    response = client.get_service_last_accessed_details(
    JobId=y
)
    #print(response['JobId'])
    #f3.write(response + "\n")
    print(response['ServicesLastAccessed'])
    tt = str(response['ServicesLastAccessed'])
    f3.write(tt + "\n")
    #with open('output.json', 'w') as outfile:
    #    json.dump(response['ServicesLastAccessed'], outfile, default=json_util.default)

for role in Job_Ids_from_file:
    HelperFun(role)
    #response = client.generate_service_last_accessed_details(
    #Arn="\"role\": \"" + role + "\""
#)    
    #print(response['JobId'])
    #f3.write(response['JobId'] + "\n")
