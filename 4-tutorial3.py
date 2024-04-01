import boto3

sqs = boto3.resource('sqs')

queue = sqs.get_queue_by_name(QueueName='test')

queue.send_message(MessageBody='boto3', MessageAttributes={
    'Author': {
        'StringValue': 'Daniel',
        'DataType': 'String'
    }
})

response = queue.send_messages(Entries=[{
    'Id': '1',
    'MessageBody': 'hello world'
},
{
    'Id': '2',
    'MessageBody': 'boto message',
    'MessageAttributes': {
        'Author': {
            'StringValue': 'Jacob',
            'DataType': 'String'
        }
    }
}])

print(response.get('Failed'))