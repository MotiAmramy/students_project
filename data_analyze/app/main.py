from flask import Flask

from data_analyze.app.db.repository.query_repository import get_gpa_hours_sleep_and_student_profile
from data_analyze.app.pandas.pandas_analyze import gpa_hours_sleep_student
from data_analyze.app.utils.convert_to_dict import convert_student_to_dict

# from flask_graphql import GraphQLView
# from graphene import Schema
# from app.gql.mutations import Mutation
# from app.gql.query import Query

app = Flask(__name__)

# schema = Schema(query=Query, mutation=Mutation)
#
# app.add_url_rule(
#    '/graphql',
#    view_func=GraphQLView.as_view(
#        'graphql',
#        schema=schema,
#        graphiql=True
#    )
# )
#


if __name__ == '__main__':
    results = get_gpa_hours_sleep_and_student_profile()
    list_of = [{**convert_student_to_dict(student), "GPA": gpa, "Sleep_Hours_Per_Day": sleep_hours} for student, gpa, sleep_hours in results]
    pa = gpa_hours_sleep_student(list_of)
    print(pa)


    app.run()