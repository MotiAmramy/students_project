import graphene
from graphene import Float, Int, String
from app.gql.types.student_type import StudentType  # Import related types

class CoursePerformanceType(graphene.ObjectType):
    id = graphene.Int()
    course_name = graphene.String()
    current_grade = graphene.Float()
    attendance_rate = graphene.Float()
    assignments_completed = graphene.Int()
    missed_deadlines = graphene.Int()
    participation_score = graphene.Float()
    midterm_grade = graphene.Float()
    study_group_attendance = graphene.Int()
    office_hours_visits = graphene.Int()
    extra_credit_completed = graphene.Int()
    student_id = graphene.String()
    student = graphene.Field(StudentType)  # Related Student Type

    @staticmethod
    def resolve_student(root, info):
        return root.student  # Resolves the related student