
from sqlalchemy.exc import SQLAlchemyError
from neo4j_consumer.app.db.psql_database import session_maker


def insert_teacher(data):
    try:
        # Create a new session for transaction
        with session_maker() as session:
            # Add the teacher object to the session and commit
            session.add(data)
            session.commit()

            # Refresh the teacher object to get the updated data (including auto-generated fields)
            session.refresh(data)

            # Return the inserted teacher object
            return data.id
    except SQLAlchemyError as e:
        # If an error occurs, rollback the transaction
        session.rollback()
        print(f"Error inserting teacher: {e}")
        return None