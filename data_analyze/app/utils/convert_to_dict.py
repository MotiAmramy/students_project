from psql_consumer.app.db.models.student import Student
from psql_consumer.app.db.models.study_metrics import StudyMetrics
from psql_consumer.app.db.models.course_performance import CoursePerformance


def convert_student_to_dict(student: Student) -> dict:
    return {
        "id": student.id,
        "first_name": student.first_name,
        "last_name": student.last_name,
        "age": student.age,
        "address": student.address

    }