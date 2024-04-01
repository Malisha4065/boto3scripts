import boto3

# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue. This returns an SQS.Queue instance
queue = sqs.get_queue_by_name(QueueName='test')

# Access identifiers and attributes
print(queue.url)
print(queue.attributes.get('DelaySeconds'))

# Print out each queue name, which is part of its ARN
for queue in sqs.queues.all():
    print(queue.url)

print("======================")
print(queue.attributes['QueueArn'].split(':')[-1])
print("======================")

# Create a new message
response = queue.send_message(MessageBody='world')

# The response is NOT a resource,but gives you a message ID and MD5
print(response.get('MessageID'))
print(response.get('MD5OfMessageBody'))