from elastic_search_comsumer.app.db.models.review import ReviewDC
from elastic_search_comsumer.app.repository.reviews_repository import insert_review_elastic_search


def topic_callback(message):
    process_messages_reviews(message.value)


def process_messages_reviews(message):
    reviews_model = [ReviewDC(**i) for i in message]
    review_inserted = insert_review_elastic_search(reviews_model)
    print(f"review inserted successfully to elastic search {review_inserted}")
