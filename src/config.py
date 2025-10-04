import os
from dotenv import load_dotenv

load_dotenv()

#environment variables and global settings
SQL_USER = os.getenv("SQL_USER", "postgres") #root for mysql
SQL_PASSWORD = os.getenv("SQL_PASSWORD", "")
SQL_HOST = os.getenv("SQL_HOST", "localhost")
SQL_PORT = os.getenv("SQL_PORT", "5432") #3306 for mysql
SQL_DATABASE = os.getenv("SQL_DATABASE", "employees")
