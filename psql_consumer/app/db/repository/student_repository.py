
from sqlalchemy.exc import SQLAlchemyError
from psql_consumer.app.db.database import session_maker

def insert_student(data):
    try:
        # Create a new session for transaction
        with session_maker() as session:
            # Add the student object to the session and commit
            session.add(data)
            session.commit()

            # Refresh the student object to get the updated data (including auto-generated fields)
            session.refresh(data)

            # Return the inserted student object id
            return data.id
    except SQLAlchemyError as e:
        # If an error occurs, rollback the transaction
        session.rollback()
        print(f"Error inserting student: {e}")
        return None