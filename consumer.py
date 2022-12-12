#!/usr/bin/env python
import sys
from argparse import ArgumentParser
from confluent_kafka import Consumer, OFFSET_BEGINNING

def reset_offset(csm, partitions) -> None:
     if args.reset:
        for p in partitions:
            p.offset = OFFSET_BEGINNING
        csm.assign(partitions)

if __name__ == '__main__':
    # Create Consumer instance
    ################
    csm = Consumer({
        'bootstrap.servers':'localhost:9092',
        'group.id':'tweet-python-consumer',
        'auto.offset.reset':'earliest'
        })
    print('Kafka Consumer has been initiated...')
    ################

    # Parse the command line.
    parser = ArgumentParser(description='> Kafka Consumer Twitter <')
    parser.add_argument('topic_to_subscribe', type=str, metavar='Tweet',
    help='Choose one of the topic above!', default='')
    parser.add_argument('--reset', action='store_true')
    args = parser.parse_args()

    # Subscribe to topic
    topic = args.topic_to_subscribe
    print('Available topics to consume: ', csm.list_topics().topics)
    csm.subscribe([topic], on_assign=reset_offset)

    # Poll for new messages from Kafka and print them.
    try:
        while True:
            msg = csm.poll(1.0)
            if msg is None:
                print("Waiting...")
            elif msg.error():
                print("ERROR: %s".format(msg.error()))
            else:
                print("Consumed event from topic {topic}: key = {key:12} value = {value:12}".format(
                    topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))
    except KeyboardInterrupt:
        pass
    finally:
        # Leave group and commit final offsets
        csm.close()