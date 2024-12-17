from neo4j_consumer.app.db.database_neo4j import driver



def insert_teacher_neo4j(teacher):
    with driver.session() as session:
        try:
            query = """
            MERGE (teacher:Teacher {
                id: $id})
            RETURN teacher.id
            """
            params = {
                "id": teacher.id,
            }
            res = session.run(query, params).single()
            return res['teacher.id']
        except Exception as e:
            print(str(e))
            return str(e)