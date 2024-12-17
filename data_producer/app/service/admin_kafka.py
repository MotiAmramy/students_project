import os
from dotenv import load_dotenv
from flask import Flask
from kafka import KafkaAdminClient
from kafka.admin import NewTopic
from kafka.errors import TopicAlreadyExistsError
import os


load_dotenv(verbose=True)



app = Flask(__name__)


def init_topics():
    client = KafkaAdminClient(bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'])
    topic_names=[
        os.environ['KAFKA_TOPIC_TEACHERS'],
        os.environ['KAFKA_TOPIC_COURSE'],
        os.environ['KAFKA_TOPIC_RELATION'],
        os.environ['KAFKA_TOPIC_STUDY_METRICS'],
        os.environ['KAFKA_TOPIC_STUDENT'],
        os.environ['KAFKA_TOPIC_TEACHERS_COURSE_PERFORMANCE'],
        os.environ['KAFKA_TOPIC_REVIEWS']
    ]

    topics = [NewTopic(
        name=topic_name,
        num_partitions=int(os.environ['NUM_PARTITIONS']),
        replication_factor=int(os.environ['REPLICATION_FACTOR'])
    ) for topic_name in topic_names]


    try:
        client.create_topics(topics)
    except TopicAlreadyExistsError as e:
        print(str(e))

    finally:
        client.close()



if __name__ == '__main__':
    init_topics()
    app.run()

