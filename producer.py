#!/usr/bin/env python
import sys
import time
import logging
import json
import twint
from argparse import ArgumentParser
from confluent_kafka import Producer

# Optional per-message delivery callback (triggered by poll() or flush())
# when a message has been successfully delivered or permanently
# failed delivery (after retries).
def delivery_callback(err, msg) -> None:
    if err:
        print(f'ERROR: Message failed delivery: {err}')
    else:
        message = '{} Produced message on topic {} with value of {}\n'.format(
            msg.key().decode('utf-8'),msg.topic(), msg.value().decode('utf-8'))
        logger.info(message)
        print(message)

def retrieve_tweet(topic: str, limit_search: int) -> None:
    # Configure Intelligent Tool
    ct = twint.Config()
    ct.Search = topic
    ct.Limit = limit_search

    # Run
    twint.run.Search(ct)

    tweets_as_objects = twint.output.tweets_object 

    for tweet in tweets_as_objects:
        msg = json.dumps(tweet)
        prd.poll(1)
        prd.produce('twitter_streaming', msg.encode('utf-8'), callback=delivery_callback)
        prd.flush()
        time.sleep(3)

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(message)s',
                        datefmt='%Y/%m/%d %H:%M:%S',
                        filename='producer.log',
                        filemode='w')

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    ####################
    # Create Producer instance
    prd = Producer({'bootstrap.servers':'localhost:9092'})
    print('Kafka Producer has been initiated...')
    ####################

    parser = ArgumentParser(description='> Kafka Streaming Twitter Custom Search Topic <')
    parser.add_argument('topic_search_term', type=str, metavar='Twitter Search',
    help='Type what you want to search for the Tweet', default='Musk')
    parser.add_argument('-L', '--limit_search', type=int, metavar='Tweet Get Limit Number',
    help='Twitter get Tweet limit', default=1000)
    args = parser.parse_args()

    retrieve_tweet(args.topic_search_term, args.limit_search)