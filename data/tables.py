import psycopg2
from dotenv import load_dotenv
import os

db_name = os.getenv('DB_NAME')
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_port = os.getenv('DB_PORT')

conn = psycopg2.connect(database=db_name,
                        host=db_host,
                        user=db_user,
                        password=db_password,
                        port=db_port)

cur = conn.cursor()

def create_tables():
    cur.execute('''
    CREATE TABLE IF NOT EXISTS movies(
            name VARCHAR(100) PRIMARY KEY,
            year INTEGER
            );''')
    cur.execute('''
    CREATE TABLE IF NOT EXISTS albums(
            name VARCHAR(100) PRIMARY KEY,
            year INTEGER
            );''')
    cur.execute('''
    CREATE TABLE IF NOT EXISTS inventions(
            name VARCHAR(100) PRIMARY KEY,
            year INTEGER
            );''')
    cur.execute('''
    CREATE TABLE IF NOT EXISTS event(
            name VARCHAR(100) PRIMARY KEY,
            year INTEGER
            );''')
    conn.commit()

create_tables()

cur.close()
conn.close()