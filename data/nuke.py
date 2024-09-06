import psycopg2

# Connect to your database
conn = psycopg2.connect(database="guessingGameDB",
                        host="localhost",
                        user="postgres",
                        password="admin",
                        port="5432")
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
