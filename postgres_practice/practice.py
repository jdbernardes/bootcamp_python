import psycopg2
import os
from dotenv import load_dotenv



def connect():
    load_dotenv()
    DB_NAME = os.environ['DB_NAME']
    DB_USER = os.environ['DB_USER']
    DB_PASS = os.environ['DB_PASS']
    DB_HOST = os.environ['DB_HOST']
    DB_PORT = os.environ['DB_PORT']
    try:
        conn = psycopg2.connect(dbname=DB_NAME, user= DB_USER, host=DB_HOST, password=DB_PASS, port = DB_PORT)
        return conn
    except Exception as e:
        print(e)
        print("I am unable to connect to the database")


def query(sql:str) -> list:
    conn = connect()
    data: list = []
    with conn.cursor() as cur:
        cur.execute(sql)
        data = cur.fetchall()
    conn.close()
    print(type(data))
    return data

def insert_simple(sql:str) -> None:
    conn = connect()
    with conn.cursor() as cur:
        cur.execute(sql)
    conn.commit()
    conn.close()

def delete(sql:str) -> None:
    conn = connect()
    with conn.cursor() as cur:
        cur.execute(sql)
    conn.commit()
    conn.close()

def update(sql:str) -> None:
    conn = connect()
    with conn.cursor() as cur:
        cur.execute(sql)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    sql = 'SELECT * FROM users'
    sql_insert = "INSERT INTO users (name, last_name, age) VALUES ('Juilo', 'Bernardes', 35)"
    sql_delete = "DELETE FROM users WHERE id = 12;"
    sql_update = "UPDATE users SET name = 'Júlio' WHERE id = 11"
    #insert_simple(sql_insert)
    #delete(sql_delete)
    #update(sql_update)
    data = query(sql)
    for user in data:
        print(f'ID: {user[0]}, Name: {user[1]}, Last Name {user[2]}, Age: {user[-1]}')