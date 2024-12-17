from dataclasses import dataclass
from typing import Optional


@dataclass
class ReviewDC:
    review_id: str
    content: str
    score: int
    thumbs_up_count: int
    review_created_version: Optional[str]  # Optional as some values are missing
    date_time: str
    app_version: Optional[str]  # Optional as some values are missing
    student_id: int



