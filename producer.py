#!/usr/bin/env python

import sys
import logging
from random import choice
from argparse import ArgumentParser
from confluent_kafka import Producer

topic_search_term = ""

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

def retrieve_tweet():
    for _ in range(50):
        data={
           'user_id': fake.random_int(min=20000, max=100000),
           'user_name':fake.name(),
           'user_address':fake.street_address() + ' | ' + fake.city() + ' | ' + fake.country_code(),
           'platform': random.choice(['Mobile', 'Laptop', 'Tablet']),
           'signup_at': str(fake.date_time_this_month())    
           }
        msg = json.dumps(data)
        prd.poll(1)
        prd.produce('user-tracker', msg.encode('utf-8'), callback=delivery_callback)
        prd.flush()
        time.sleep(3)

if __name__ == '__main__':
    parser = ArgumentParser(description='> Kafka Streaming Twitter Custom Search Topic <')
    parser.add_argument('topic_search_term', type=str, metavar='Twitter Search',
    help='Type what you want to search for the Tweet', default='')
    args = parser.parse_args()

    retrieve_tweet()