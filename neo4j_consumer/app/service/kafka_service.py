from neo4j_consumer.app.db.models.neo4j_models import CourseDC, RelationDC, TeacherDC, StudentDC
from neo4j_consumer.app.db.models.sql_models import Course, Teacher
from neo4j_consumer.app.db.repository.neo4j_repository.course_repository import create_teacher_course_relation
from neo4j_consumer.app.db.repository.neo4j_repository.relatiom_repository import create_student_course_relation
from neo4j_consumer.app.db.repository.neo4j_repository.student_repository import insert_student_neo4j
from neo4j_consumer.app.db.repository.neo4j_repository.teacher_repository import insert_teacher_neo4j
from neo4j_consumer.app.db.repository.psql_repository.course_repository import insert_course
from neo4j_consumer.app.db.repository.psql_repository.teacher_repository import insert_teacher
import os
from dotenv import load_dotenv


load_dotenv(verbose=True)





def process_messages_teacher(message):
    for i in message:
        sql_teacher = Teacher(**i)
        sql_teacher_inserted = insert_teacher(sql_teacher)
        print(f"teacher inserted successfully to sql {sql_teacher_inserted}")
        nep4j_teacher = TeacherDC(i['id'])
        nep4j_teacher_inserted = insert_teacher_neo4j(nep4j_teacher)
        print(f"teacher inserted successfully to neo4j {nep4j_teacher_inserted}")
    return



def process_messages_course(message):
    for i in message:
        sql_course = Course(**i)
        sql_course_inserted = insert_course(sql_course)
        print(f"course inserted successfully to sql {sql_course_inserted}")
        nep4j_course = CourseDC(i['id'])
        neo4j_teacher = TeacherDC(i['teacher_id'])
        nep4j_course_inserted = create_teacher_course_relation(nep4j_course, neo4j_teacher)
        print(f"course inserted successfully to neo4j {nep4j_course_inserted}")
    return


def process_messages_relation(message):
    for i in message:
        nep4j_student = StudentDC(i['student_id'])
        nep4j_student_inserted = insert_student_neo4j(nep4j_student)
        print(f"student inserted successfully to neo4j {nep4j_student_inserted}")
        neo4j_relation = RelationDC(**i)
        relation_student_course = create_student_course_relation(neo4j_relation)
        print(f"relation inserted successfully to neo4j {relation_student_course}")
    return





def topic_callback(message):
    topic = message.topic
    if topic == os.environ['KAFKA_TOPIC_TEACHERS']:
        process_messages_teacher(message.value)
    elif topic == os.environ['KAFKA_TOPIC_COURSE']:
        process_messages_course(message.value)
    elif topic == os.environ['KAFKA_TOPIC_RELATION']:
        process_messages_relation(message.value)
    else:
        print(f"Unknown topic: {topic}")

