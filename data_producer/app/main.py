from data_producer.app.service.elastic_search_producer import produce_csv_data_to_elastic_search
from data_producer.app.service.neo4j_producer import produce_to_neo4j
from data_producer.app.service.psql_producer import produce_csv_data_to_psql




if __name__ == '__main__':
    produce_to_neo4j()
    produce_csv_data_to_psql()
    # produce_csv_data_to_elastic_search()

