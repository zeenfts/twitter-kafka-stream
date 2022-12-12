FROM python:3.8.16-slim-bullseye
LABEL maintainer="zeenfts"

ENV KAFKA_HOME=/usr/twitter_kafka_stream

RUN python -m pip install --upgrade pip setuptools wheel --no-cache-dir

WORKDIR $KAFKA_HOME
# VOLUME /usr

user root
RUN rm -rf /.dbt
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x ./script/run_app.sh