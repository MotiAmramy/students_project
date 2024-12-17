from neo4j_consumer.app.db.database_neo4j import driver





def insert_student_neo4j(student):
    with driver.session() as session:
        try:
            query = """
            MERGE (student:Student {id: $id})
            RETURN student.id
            """
            params = {
                "id": student.id
            }
            res = session.run(query, params).single()
            return res['student.id']
        except Exception as e:
            print(str(e))
            return str(e)