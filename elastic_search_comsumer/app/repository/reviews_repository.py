from elastic_search_comsumer.app.db.database import connect_elasticsearch
from elasticsearch import helpers

def insert_review_elastic_search(reviews_model):
    with connect_elasticsearch() as es_client:
        es_documents = [to_elasticsearch_doc(review) for review in reviews_model]

        # Bulk insert into Elasticsearch
        try:
            helpers.bulk(es_client, es_documents)
            print(f"Successfully inserted {len(es_documents)} reviews into Elasticsearch.")
        except Exception as e:
            print(f"Error inserting data into Elasticsearch: {e}")
    return "finished inserting data into Elasticsearch"





def to_elasticsearch_doc(review):
    """Convert Review instance into Elasticsearch-compatible dictionary."""
    return {
        "_index": "reviews",
        "_id": review.review_id,  # Use review_id as the document ID
        "_source": {
            "content": review.content,
            "score": review.score,
            "thumbs_up_count": review.thumbs_up_count,
            "review_created_version": review.review_created_version,
            "date_time": review.date_time,  # Convert to ISO format
            "app_version": review.app_version,
            "student_id": review.student_id,
        },
    }