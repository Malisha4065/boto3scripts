import boto3

s3 = boto3.resource('s3')

# print out the bucket names
for bucket in s3.buckets.all():
    print(bucket.name)


# # upload a new file
# with open('test.jpg', 'rb') as data:
#     s3.Bucket('my-bucket').put_object(Key='test.jpg', Body=data)