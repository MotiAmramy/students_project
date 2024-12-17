from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from neo4j_consumer.app.db.models.sql_models import Base

load_dotenv(verbose=True)


engine = create_engine(os.environ['POSTGRESQL_URL'])
session_maker = sessionmaker(bind=engine)




def init_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)



