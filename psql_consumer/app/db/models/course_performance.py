from sqlalchemy import Column, Integer, String, Float, ForeignKey
from psql_consumer.app.db.models import Base
from sqlalchemy.orm import relationship



class CoursePerformance(Base):
    __tablename__ = 'course_performance'
    id = Column(Integer, primary_key=True, autoincrement=True)
    course_name = Column(String, nullable=False)
    current_grade = Column(Float, nullable=False)
    attendance_rate = Column(Float, nullable=False)
    assignments_completed = Column(Integer, nullable=False)
    missed_deadlines = Column(Integer, nullable=False)
    participation_score = Column(Float, nullable=False)
    midterm_grade = Column(Float, nullable=False)
    study_group_attendance = Column(Integer, nullable=False)
    office_hours_visits = Column(Integer, nullable=False)
    extra_credit_completed = Column(Integer, nullable=False)
    student_id = Column(String, ForeignKey('students.id'), nullable=False)

    student = relationship('Student', back_populates='course_performances')

    def __repr__(self):
        return (f"<CoursePerformance(student_id={self.student_id}, "
                f"course_name='{self.course_name}', current_grade={self.current_grade}, "
                f"attendance_rate={self.attendance_rate}, assignments_completed={self.assignments_completed}, "
                f"missed_deadlines={self.missed_deadlines}, participation_score={self.participation_score}, "
                f"midterm_grade={self.midterm_grade}, study_group_attendance={self.study_group_attendance}, "
                f"office_hours_visits={self.office_hours_visits}, "
                f"extra_credit_completed={self.extra_credit_completed})>")