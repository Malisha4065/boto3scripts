# Describe regions and availability zones
import boto3

ec2 = boto3.client('ec2')

# Retrieves all regions/endpoints that work with ec2
response = ec2.describe_regions()
print('Regions:', response['Regions'])

print('==============================================')

# Retrieves availability zones only for region of the ec2 object
response = ec2.describe_availability_zones()
print('Availability Zones:', response['AvailabilityZones'])