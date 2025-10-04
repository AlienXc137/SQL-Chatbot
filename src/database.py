from langchain_community.utilities import SQLDatabase

#database connection
# def init_database(user: str, password: str, host: str, port: str, database: str) -> SQLDatabase:
#     #db_uri = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
#     db_uri = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
#     return SQLDatabase.from_uri(db_uri)

def init_database(user: str, password: str, host: str, port: str, database: str) -> SQLDatabase:
    db_uri = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
    return SQLDatabase.from_uri(db_uri, include_tables=None, sample_rows_in_table_info=2, schema=database)

