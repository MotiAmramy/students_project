from typing import List, Any

from data_producer.app.data.read_data import read_csv
import os
from dotenv import load_dotenv
from data_producer.app.service.producer import produce


load_dotenv(verbose=True)

def produce_csv_data_to_psql():
    student_course_path = get_student_course_path()
    student_lifestyle_path = get_student_lifestyle_path()
    student_profiles_path = get_student_profiles_path()

    publish_student_profiles(student_profiles_path)
    publish_course_performance(student_course_path)
    publish_lifestyle_metrics(student_lifestyle_path)

def get_student_course_path() -> str:
    return os.path.join(os.path.dirname(__file__), '../../../', 'proj_data', 'student_course_performance.csv')

def get_student_lifestyle_path() -> str:
    return os.path.join(os.path.dirname(__file__), '../../../', 'proj_data', 'student_lifestyle.csv')

def get_student_profiles_path() -> str:
    return os.path.join(os.path.dirname(__file__), '../../../', 'proj_data', 'students-profiles.csv')

def publish_course_performance(file_path: str):
    csv_data = read_csv(file_path)
    chunked_data = list(split_into_chunks(csv_data, 100))
    for chunk in chunked_data:
        produce(chunk, 'course_performance', os.environ['KAFKA_TOPIC_TEACHERS_COURSE_PERFORMANCE'])
        print("Published to Neo4j: Course Performance in chunks")

def publish_lifestyle_metrics(file_path: str):
    csv_data = read_csv(file_path)
    chunked_data = list(split_into_chunks(csv_data, 100))
    for chunk in chunked_data:
        produce(chunk, 'study_metrics', os.environ['KAFKA_TOPIC_STUDY_METRICS'])
        print("Published to Neo4j: Lifestyle Metrics in chunks")

def publish_student_profiles(file_path: str):
    csv_data = read_csv(file_path)
    chunked_data = list(split_into_chunks(csv_data, 100))
    for chunk in chunked_data:
        produce(chunk, 'student', os.environ['KAFKA_TOPIC_STUDENT'])
        print("Published to Neo4j: Student Profiles in chunks")



def split_into_chunks(data: List[Any], chunk_size: int):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]
