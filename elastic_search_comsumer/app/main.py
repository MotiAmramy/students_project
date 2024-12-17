from flask import Flask
from elastic_search_comsumer.app.service.consumer import consume_topic, topic
from elastic_search_comsumer.app.service.kafka_service import topic_callback

app = Flask(__name__)

if __name__ == '__main__':
    # init_db()
    consume_topic(topic, topic_callback)
    app.run(debug=True)
