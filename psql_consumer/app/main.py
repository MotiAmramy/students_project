from flask import Flask

from psql_consumer.app.db.database import init_db
from psql_consumer.app.db.models.course_performance import CoursePerformance
from psql_consumer.app.service.consumer import consume_topic, topics
from psql_consumer.app.service.kafka_service import topic_callback


app = Flask(__name__)





if __name__ == '__main__':
    # init_db()
    consume_topic(topics, topic_callback)
    app.run(debug=True)
    # a = {'student_id': '934'
    #     , 'course_name': 'Mathematics 201'
    #     , 'current_grade': '69.85'
    #     , 'attendance_rate': '70.3'
    #     , 'assignments_completed': '11'
    #     , 'missed_deadlines': '0'
    #     , 'participation_score': '74.22'
    #     , 'midterm_grade': '68.03'
    #     , 'study_group_attendance': '3'
    #     , 'office_hours_visits': '3'
    #     , 'extra_credit_completed': '1'}
    # b = CoursePerformance(**a)
    # print(b)
