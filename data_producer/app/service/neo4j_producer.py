from data_producer.app.data.read_data import read_json
import os
from dotenv import load_dotenv
from data_producer.app.service.producer import produce


load_dotenv(verbose=True)

from typing import List, Any

def produce_to_neo4j():
    academic_network_path = get_academic_network_path()
    json_data = read_json(academic_network_path)

    publish_teachers(json_data['teachers'])
    publish_classes(json_data['classes'])
    publish_relationships(json_data['relationships'])

def get_academic_network_path() -> str:
    return os.path.join(os.path.dirname(__file__), '../../../', 'proj_data', 'academic_network.json')

def publish_teachers(teachers_data: Any):
    produce(teachers_data, 'teachers', os.environ['KAFKA_TOPIC_TEACHERS'])
    print("Published to Neo4j: Teachers")

def publish_classes(classes_data: Any):
    produce(classes_data, 'classes', os.environ['KAFKA_TOPIC_COURSE'])
    print("Published to Neo4j: Classes")

def publish_relationships(relationships_data: List[Any]):
    chunked_data = list(split_into_chunks(relationships_data, 100))
    for chunk in chunked_data:
        produce(chunk, 'relationships', os.environ['KAFKA_TOPIC_RELATION'])
        print("Published to Neo4j: Relationships in chunks")

def split_into_chunks(data: List[Any], chunk_size: int):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]



