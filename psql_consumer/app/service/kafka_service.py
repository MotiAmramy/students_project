from psql_consumer.app.db.models.course_performance import CoursePerformance
from psql_consumer.app.db.models.student import Student
from psql_consumer.app.db.models.study_metrics import StudyMetrics
from psql_consumer.app.db.repository.course_performance_repository import insert_course_performance
from psql_consumer.app.db.repository.student_repository import insert_student
from psql_consumer.app.db.repository.study_metrics_repository import insert_study_metrics
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)


def process_messages_student(message):
    for i in message:
        student = Student(**i)
        inserted_student =  insert_student(student)
        print(f"student inserted successfully to sql {inserted_student}")



def process_messages_course_performance(message):
    for i in message:
        course_performance = CoursePerformance(**i)
        inserted_course_performance =  insert_course_performance(course_performance)
        print(f"course_performance inserted successfully to sql {inserted_course_performance}")


def process_messages_study_metrics(message):
    for i in message:
        study_metrics = StudyMetrics(**i)
        inserted_study_metrics =  insert_study_metrics(study_metrics)
        print(f"study_metrics inserted successfully to sql {inserted_study_metrics}")





def topic_callback(message):
    topic = message.topic
    if topic == os.environ['KAFKA_TOPIC_TEACHERS_COURSE_PERFORMANCE']:
        process_messages_course_performance(message.value)
    elif topic == os.environ['KAFKA_TOPIC_STUDENT']:
        process_messages_student(message.value)
    elif topic == os.environ['KAFKA_TOPIC_STUDY_METRICS']:
        process_messages_study_metrics(message.value)
    else:
        print(f"Unknown topic: {topic}")
