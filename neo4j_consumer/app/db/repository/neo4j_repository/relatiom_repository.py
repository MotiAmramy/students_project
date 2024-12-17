from neo4j_consumer.app.db.database_neo4j import driver


def create_student_course_relation(relation):
    with driver.session() as session:
        try:
            query = """
            MERGE (student:Student {id: $student_id})
            MERGE (course:Course {id: $class_id})
            MERGE (student)-[:ENROLLED_IN {
                enrollment_date: $enrollment_date,
                relationship_type: $relationship_type
            }]->(course)
            RETURN student.id, course.id
            """
            params = {
                "student_id": relation.student_id,
                "class_id": relation.class_id,
                "enrollment_date": relation.enrollment_date,
                "relationship_type": relation.relationship_type,
            }
            res = session.run(query, params).single()
            return res['course.id']
        except Exception as e:
            print(str(e))
            return str(e)