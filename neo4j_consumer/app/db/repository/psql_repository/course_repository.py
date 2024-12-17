
from sqlalchemy.exc import SQLAlchemyError
from neo4j_consumer.app.db.psql_database import session_maker


def insert_course(data):
    try:
        # Create a new session for transaction
        with session_maker() as session:

            # Add the course object to the session and commit
            session.add(data)
            session.commit()

            # Refresh the course object to get the updated data (including auto-generated fields)
            session.refresh(data)

            # Return the inserted course object
            return data.id
    except SQLAlchemyError as e:
        # If an error occurs, rollback the transaction
        session.rollback()
        print(f"Error inserting course: {e}")
        return None