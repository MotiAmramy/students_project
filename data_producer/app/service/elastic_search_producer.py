from typing import List, Any
from data_producer.app.data.read_data import read_csv
import os
from dotenv import load_dotenv
from data_producer.app.service.producer import produce


load_dotenv(verbose=True)

def produce_csv_data_to_elastic_search():
    reviews_path = get_review_path()
    publish_reviews(reviews_path)


def get_review_path() -> str:
    reviews_with_students = os.path.join(os.path.dirname(__file__), '../../../', 'proj_data', 'reviews_with_students.csv')
    return reviews_with_students



def publish_reviews(file_path: str):
    csv_data = read_csv(file_path)
    chunked_data = list(split_into_chunks(csv_data, 100))
    for chunk in chunked_data:
        produce(chunk, 'reviews', os.environ['KAFKA_TOPIC_REVIEWS'])
        print("Published to elastic search: reviews in chunks")



def split_into_chunks(data: List[Any], chunk_size: int):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]
