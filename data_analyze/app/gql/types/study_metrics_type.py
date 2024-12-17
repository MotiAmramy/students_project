from graphene import Float, String, Int, Field, ObjectType


class StudyMetricsType(ObjectType):
    id = Int()
    study_hours_per_day = Float()
    extracurricular_hours_per_day = Float()
    sleep_hours_per_day = Float()
    social_hours_per_day = Float()
    physical_activity_hours_per_day = Float()
    gpa = Float()
    stress_level = String()
    student_id = String()
    student = Field('app.gql.types.student_type.StudentType')  # Related Student Type

    @staticmethod
    def resolve_student(root, info):
        return root.student  # Resolves the related student