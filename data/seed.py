import psycopg2
from dotenv import load_dotenv
import os
import json

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

def seed(json_file):
    with open(json_file, "r") as f:
        data = json.load(f)

        # Insert data into movies, albums, inventions, and event tables
    for year, details in data.items():
        movie_name = details.get("movie")
        album_name = details.get("album")
        invention_name = details.get("invention")
        event_name = details.get("event")
        
        # Insert into movies table
        cur.execute('''
            INSERT INTO movies (name, year)
            VALUES (%s, %s) ON CONFLICT (name) DO NOTHING;
        ''', (movie_name, year))

        # Insert into albums table
        cur.execute('''
            INSERT INTO albums (name, year)
            VALUES (%s, %s) ON CONFLICT (name) DO NOTHING;
        ''', (album_name, year))

        # Insert into inventions table
        cur.execute('''
            INSERT INTO inventions (name, year)
            VALUES (%s, %s) ON CONFLICT (name) DO NOTHING;
        ''', (invention_name, year))

        # Insert into event table
        cur.execute('''
            INSERT INTO event (name, year)
            VALUES (%s, %s) ON CONFLICT (name) DO NOTHING;
        ''', (event_name, year))

    # Commit the changes
    conn.commit()

seed("C:/Users/Domin/Documents/GitHub/guessingGameAPI/data/data.json") #only works with absolute path apparently

cur.close()
conn.close()