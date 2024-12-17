from dotenv import load_dotenv
from kafka import KafkaConsumer
import json
import os


load_dotenv(verbose=True)


def consume_topic(topics: list, process_message_callback):

    consumer = KafkaConsumer(
        *topics,
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    for message in consumer:
        process_message_callback(message)

topics = [
    os.environ['KAFKA_TOPIC_TEACHERS'],
    os.environ['KAFKA_TOPIC_COURSE'],
    os.environ['KAFKA_TOPIC_RELATION']
]


