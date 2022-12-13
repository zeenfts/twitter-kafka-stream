# twitter-kafka-stream
Consume Tweet "" using Kafka Basic Component from Twitter API.

Info:
1. `docker compose up` and see the log on terminal.
2. If error persist (esp the app-producer & app-consumer) just keep the containers running & continue to step 3. If not, observe the log then just skip to last step (7).
3. Install dependencies from [requirements.txt](https://github.com/zeenfts/twitter-kafka-stream/blob/main/requirements.txt).
4. If error again check the [docker/Dockerfile](https://github.com/zeenfts/twitter-kafka-stream/blob/main/docker/Dockerfile) on line 14 & 15.
5. Run [app/producer.py {optional args1 -S topic to search} {optional args2 -L limit search}](https://github.com/zeenfts/twitter-kafka-stream/blob/main/app/producer.py) and [app/consumer.py](https://github.com/zeenfts/twitter-kafka-stream/blob/main/app/consumer.py).
6. It should be a successful running, now. Don't forget to stop all the containers at the end.
7. You will get something as shown: [imgs](https://github.com/zeenfts/twitter-kafka-stream/tree/main/imgs) and [data](https://github.com/zeenfts/twitter-kafka-stream/tree/main/data) (only if the container failed).
