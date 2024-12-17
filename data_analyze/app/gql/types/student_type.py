from graphene import ObjectType, Int, String, List


class StudentType(ObjectType):
    id = String()
    first_name = String()
    last_name = String()
    age = Int()
    address = String()
    study_metrics = List('app.gql.types.study_metrics_type.StudyMetricType')
    course_performances = List('app.gql.types.course_performance_type.CoursePerformanceType')

    @staticmethod
    def resolve_study_metrics(root, info):
        # Assuming `root` is a Student instance, this will resolve the related study metrics
        return root.study_metrics

    @staticmethod
    def resolve_course_performances(root, info):
        # Assuming `root` is a Student instance, this will resolve the related course performances
        return root.course_performances


