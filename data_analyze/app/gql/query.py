from graphene import ObjectType, Field, List, Int, String, Float

from data_analyze.app.db.repository.query_repository import get_gpa_hours_sleep_and_student_profile


# class Query(ObjectType):
#     gpa_sleep_hours_per_student = List(,)

    #
    # @staticmethod
    # def resolve_gpa_sleep_hours_per_student(root, info, start_date, end_date):
    #     return get_gpa_hours_sleep_and_student_profile()