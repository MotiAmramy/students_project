from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from neo4j_consumer.app.db.models.sql_models import Base



class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    department = Column(String, nullable=False)
    title = Column(String, nullable=False)
    office = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    # Relationship to access courses taught by the teacher
    courses = relationship("Course", back_populates="teacher")

    def __repr__(self):
        return (f"<Teacher(id='{self.id}', name='{self.name}', "
                f"department='{self.department}', title='{self.title}', "
                f"office='{self.office}', email='{self.email}')>")


