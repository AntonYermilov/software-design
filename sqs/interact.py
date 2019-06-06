import sys
import boto3
import time

option, nameA, nameB = sys.argv[1:]
sqs = boto3.resource('sqs', endpoint_url='http://localstack:4576/')

if option == '--initialize':
    while True:
        try:
            sqs.create_queue(QueueName=nameA).send_message(MessageBody='1')
            sqs.create_queue(QueueName=nameB)
        except:
            time.sleep(1)
            continue
        break

    print('queues successfully created')
    exit(0)

if option == '--interact':
    queueA, queueB = None, None

    while True:
        try:
            queueA = sqs.get_queue_by_name(QueueName=nameA)
            queueB = sqs.get_queue_by_name(QueueName=nameB)
        except:
            time.sleep(1)
            continue
        break

    assert queueA is not None
    assert queueB is not None

    while True:
        for msg in queueA.receive_messages():
            num = int(msg.body)
            print(num, flush=True)
            queueB.send_message(MessageBody=str(num+1))
            msg.delete()
            time.sleep(1)
    exit(0)
