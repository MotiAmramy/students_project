from datetime import datetime
from dataclasses import dataclass


@dataclass
class RelationDC:
    student_id: str
    class_id: str
    teacher_id: str
    enrollment_date: str
    relationship_type: str