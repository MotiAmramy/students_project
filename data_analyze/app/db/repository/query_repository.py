from data_analyze.app.db.psql_database import session_maker
from psql_consumer.app.db.models.student import Student
from psql_consumer.app.db.models.study_metrics import StudyMetrics


def get_gpa_hours_sleep_and_student_profile():
    with session_maker() as session:
        try:
            results = session.query(Student, StudyMetrics.GPA, StudyMetrics.Sleep_Hours_Per_Day).join(StudyMetrics, Student.id == StudyMetrics.Student_ID).all()
            return results
        except Exception as e:
            print(str(e))
            return None



