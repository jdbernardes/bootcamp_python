from sqlalchemy import create_engine, insert, text
import time

time.sleep(5)

engine = create_engine("postgresql+psycopg2://postgres:postgres@db_julio:5432")
conn = engine.connect()
query=text("INSERT INTO users (name, last_name, age) VALUES ('John', 'Doe', 30)")
conn.execute(query)
conn.commit()

print('done')