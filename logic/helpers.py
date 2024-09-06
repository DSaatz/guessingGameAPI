import random
import psycopg2

conn = psycopg2.connect(database="guessingGameDB",
                        host="localhost",
                        user="postgres",
                        password="admin",
                        port="5432")

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