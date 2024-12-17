from neo4j_consumer.app.db.database_neo4j import driver









def create_teacher_course_relation(nep4j_course, neo4j_teacher):
    with driver.session() as session:
        try:
            query = """
            MERGE (teacher:Teacher {id: $teacher_id})
            MERGE (course:Course {id: $id})
            MERGE (teacher)-[:TEACHES]->(course)
            RETURN teacher.id, course.id
            """
            params = {
                "teacher_id": neo4j_teacher.id,
                "id": nep4j_course.id,
                }
            res = session.run(query, params).single()
            return res['course.id']
        except Exception as e:
            print(str(e))
            return str(e)