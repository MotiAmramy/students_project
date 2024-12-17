from sqlalchemy import Column, String, Float, Integer, ForeignKey
from psql_consumer.app.db.models import Base
from sqlalchemy.orm import relationship



class StudyMetrics(Base):
    __tablename__ = 'study_metrics'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Study_Hours_Per_Day = Column(Float, nullable=False)
    Extracurricular_Hours_Per_Day = Column(Float, nullable=False)
    Sleep_Hours_Per_Day = Column(Float, nullable=False)
    Social_Hours_Per_Day = Column(Float, nullable=False)
    Physical_Activity_Hours_Per_Day = Column(Float, nullable=False)
    GPA = Column(Float, nullable=False)
    Stress_Level = Column(String, nullable=False)
    Student_ID = Column(String, ForeignKey("students.id"))

    student = relationship('Student', back_populates='study_metrics', )

    def __repr__(self):
        return (f"<StudyMetrics(Student_ID={self.Student_ID}, "
                f"Study_Hours_Per_Day={self.Study_Hours_Per_Day}, "
                f"Extracurricular_Hours_Per_Day={self.Extracurricular_Hours_Per_Day}, "
                f"Sleep_Hours_Per_Day={self.Sleep_Hours_Per_Day}, "
                f"Social_Hours_Per_Day={self.Social_Hours_Per_Day}, "
                f"Physical_Activity_Hours_Per_Day={self.Physical_Activity_Hours_Per_Day}, "
                f"GPA={self.GPA}, Stress_Level='{self.Stress_Level}')>")