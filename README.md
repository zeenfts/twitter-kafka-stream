# twitter-kafka-stream
Consume Tweet with Keyword "Kaesang" using Kafka Basic Component from Twitter API.

Info:
1. `docker compose up` and see the log on terminal.
2. `docker logs --follow app-producer` on new terminal. Please look at after 'Producer App Twitter Post'. Long setup ~5 minutes, please be patience. Tweaks the args parameter inside [docker-compose.yaml](https://github.com/zeenfts/twitter-kafka-stream/blob/main/docker-compose.yaml#L24) on line 24.
3. `docker logs --follow app-consumer` on new terminal. Please look at after 'Consumer App Twitter Get'.
4. After a while, the apps should be running (you'll see that consumer-app start first just wait till the topics ready). Don't forget to stop all the containers at the end.
5. You will get something as shown: [imgs/](https://github.com/zeenfts/twitter-kafka-stream/tree/main/imgs) and [logs/](https://github.com/zeenfts/twitter-kafka-stream/tree/main/logs).
