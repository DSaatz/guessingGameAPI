import psycopg2

conn = psycopg2.connect(database="guessingGameDB",
                        host="localhost",
                        user="postgres",
                        password="admin",
                        port="5432")

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