import random
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

def randomYear():
    return random.randint(1948, 2020)

def extract_string(tuple_list):
    # Extract the string from the first tuple in the list
    if tuple_list and isinstance(tuple_list[0], tuple) and len(tuple_list[0]) > 0:
        return tuple_list[0][0]
    return None  # Or raise an exception if appropriate

def movieFromYear(year):
    cur.execute('SELECT name FROM movies WHERE year = %s', (year,))
    return extract_string(cur.fetchall())

def albumFromYear(year):
    cur.execute('SELECT name FROM albums WHERE year = %s', (year,))
    return extract_string(cur.fetchall())

def inventionFromYear(year):
    cur.execute('SELECT name FROM inventions WHERE year = %s', (year,))
    return extract_string(cur.fetchall())

def eventFromYear(year):
    cur.execute('SELECT name FROM event WHERE year = %s', (year,))
    return extract_string(cur.fetchall())
