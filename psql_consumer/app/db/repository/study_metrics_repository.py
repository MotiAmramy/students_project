from sqlalchemy.exc import SQLAlchemyError

from psql_consumer.app.db.database import session_maker


def insert_study_metrics(data):
    try:
        # Create a new session for transaction
        with session_maker() as session:
            # Add the study metrics object to the session and commit
            session.add(data)
            session.commit()

            # Refresh the study metrics object to get the updated data (including auto-generated fields)
            session.refresh(data)

            # Return the inserted study metrics object id
            return data.id
    except SQLAlchemyError as e:
        # If an error occurs, rollback the transaction
        session.rollback()
        print(f"Error inserting study metrics: {e}")
        return None