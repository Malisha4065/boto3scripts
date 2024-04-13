# Describe key pairs

import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_key_pairs()
print(response)

# create key pair
response2 = ec2.create_key_pair(KeyName='KEY_PAIR_NAME')
print(response2)

# delete a key pair
response3 = ec2.delete_key_pair(KeyName='KEY_PAIR_NAME')
print(response3)