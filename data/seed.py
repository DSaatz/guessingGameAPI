import psycopg2
import json

conn = psycopg2.connect(database="guessingGameDB",
                        host="localhost",
                        user="postgres",
                        password="admin",
                        port="5432")

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