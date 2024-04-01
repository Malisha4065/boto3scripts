import boto3

# Get the service resource
sqs = boto3.resource('sqs')

# Create te queue. This returns an SQS instance
queue  =sqs.create_queue(QueueName='test', Attributes={'DelaySeconds': '5'})

# Access identifiers and attributes
print(queue.url)
print(queue.attributes.get('DelaySeconds'))
