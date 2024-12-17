
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
        print(message)
        process_message_callback(message)

topics = [
    os.environ['KAFKA_TOPIC_STUDY_METRICS'],
    os.environ['KAFKA_TOPIC_STUDENT'],
    os.environ['KAFKA_TOPIC_TEACHERS_COURSE_PERFORMANCE']
]
