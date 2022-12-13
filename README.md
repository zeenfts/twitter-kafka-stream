# twitter-kafka-stream
Consume Tweet "" using Kafka Basic Component from Twitter API.

Info:
1. `docker compose up`
2. If error just keep the containers running, then make virtual environment of python (or just skip to step 3).
3. Install dependencies from [requirements.txt](https://github.com/zeenfts/twitter-kafka-stream/blob/main/requirements.txt).
4. If error again check the [Docker file](https://github.com/zeenfts/twitter-kafka-stream/blob/main/docker/Dockerfile) on line 14 & 15.
5. Run [.app/producer.py {optional args1 -S topic to search} {optional args2 -L limit search}](https://github.com/zeenfts/twitter-kafka-stream/blob/main/app/producer.py) and [./app/consumer.py](https://github.com/zeenfts/twitter-kafka-stream/blob/main/app/consumer.py).
6. It should be a successful running, now. Don't forget to stop all the containers at the end.
7. You will get something as shown: [imgs](https://github.com/zeenfts/twitter-kafka-stream/tree/main/imgs) and [data](https://github.com/zeenfts/twitter-kafka-stream/tree/main/data).