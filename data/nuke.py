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

# Function to drop all tables
def drop_all_tables():
    cur.execute("""
    DO $$ 
    DECLARE
        r RECORD;
    BEGIN
        FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = 'public') 
        LOOP
            EXECUTE 'DROP TABLE IF EXISTS public.' || r.tablename || ' CASCADE;';
        END LOOP;
    END $$;
    """)
    conn.commit()

# Call the function
drop_all_tables()

# Close the connection
cur.close()
conn.close()
