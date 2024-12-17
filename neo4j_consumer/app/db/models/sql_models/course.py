from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from neo4j_consumer.app.db.models.sql_models import Base


class Course(Base):
    __tablename__ = 'courses'
    id = Column(String, primary_key=True)
    course_name = Column(String, nullable=False)
    section = Column(String, nullable=False)
    department = Column(String, nullable=False)
    semester = Column(String, nullable=False)
    room = Column(String, nullable=False)
    schedule = Column(String, nullable=False)
    teacher_id = Column(String, ForeignKey('teachers.id'), nullable=False)

    # Relationship to access teacher from a course
    teacher = relationship("Teacher", back_populates="courses")

    def __repr__(self):
        return (f"<Course(id='{self.id}', course_name='{self.course_name}', "
                f"section='{self.section}', department='{self.department}', "
                f"semester='{self.semester}', room='{self.room}', "
                f"schedule='{self.schedule}', teacher_id='{self.teacher_id}')>")

