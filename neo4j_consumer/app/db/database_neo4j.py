from dotenv import load_dotenv
from neo4j import GraphDatabase
import os


load_dotenv(verbose=True)

# connection for neo4j
driver = GraphDatabase.driver(
    os.environ['NEO4J_URI'],
    auth=(os.environ['NEO4J_USER'],os.environ['NEO4J_PASSWORD'])
)







