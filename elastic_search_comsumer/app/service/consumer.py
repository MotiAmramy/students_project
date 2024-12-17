from dotenv import load_dotenv
from kafka import KafkaConsumer
import json
import os


load_dotenv(verbose=True)


def consume_topic(topic, process_message_callback):

    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    for message in consumer:
        process_message_callback(message)

topic = os.environ['KAFKA_TOPIC_REVIEWS']

