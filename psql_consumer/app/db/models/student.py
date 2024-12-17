from sqlalchemy import Column, Integer, String
from psql_consumer.app.db.models import Base
from sqlalchemy.orm import relationship



class Student(Base):
    __tablename__ = 'students'
    id = Column(String, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    address = Column(String, nullable=False)

    study_metrics = relationship('StudyMetrics', back_populates='student', lazy='joined')
    course_performances = relationship('CoursePerformance', back_populates='student', lazy='joined')

    def __repr__(self):
        return (f"<Student(id={self.id}, first_name='{self.first_name}', "
                f"last_name='{self.last_name}', age={self.age}, "
                f"address='{self.address}')>")