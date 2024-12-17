from sqlalchemy.orm import declarative_base
Base = declarative_base()

from .teacher import Teacher
from .course import Course
