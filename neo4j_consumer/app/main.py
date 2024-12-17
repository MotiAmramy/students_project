from flask import Flask
from neo4j_consumer.app.service.consumer import topics, consume_topic
from neo4j_consumer.app.db.psql_database import init_db
from neo4j_consumer.app.service.kafka_service import topic_callback








app = Flask(__name__)

if __name__ == '__main__':
    init_db()
    consume_topic(topics, topic_callback)
    app.run(debug=True)
