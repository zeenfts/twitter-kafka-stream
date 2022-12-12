# twitter-kafka-stream
Consume Tweet "" using Kafka Basic Component from Twitter API.

Info:
1. Create Topic
  docker compose exec broker \
    kafka-topics --create \
      --topic purchases \
      --bootstrap-server localhost:9092 \
      --replication-factor 1 \
      --partitions 1