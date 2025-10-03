import os
from dotenv import load_dotenv

load_dotenv()

#environment variables and global settings
SQL_USER = os.getenv("SQL_USER", "root")
SQL_PASSWORD = os.getenv("SQL_PASSWORD", "")
SQL_HOST = os.getenv("SQL_HOST", "localhost")
SQL_PORT = os.getenv("SQL_PORT", "3306")
SQL_DATABASE = os.getenv("SQL_DATABASE", "chinook")
