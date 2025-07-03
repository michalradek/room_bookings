import sqlite3
from contextlib import contextmanager
import bcrypt


DB_PATH = "backend.sqlite3"

@contextmanager
def db_connection():
    conn = sqlite3.connect(DB_PATH)
    try:
        yield conn
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

def check_database(table_name, column):
    allowed_tables = {"users", "rooms"}
    if table_name not in allowed_tables:
        raise ValueError("Invalid table name")
    with db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
            {column}
            )""")
    

def login(username, password):
    with db_connection() as conn:
        cursor = conn.cursor()
        check_database("users", "id INTEGER PRIMARY KEY, username TEXT, passwd BLOB")
        cursor.execute(f"SELECT passwd FROM users where username = {username}")

def create_user(username, password):
        with db_connection() as conn:
            check_database("users", "id INTEGER PRIMARY KEY, username TEXT UNIQUE NOT NULL, passwd text")
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
            existing = cursor.fetchone()
            if existing:
                raise ValueError("User already exist")
            cursor.execute(
                "INSERT INTO users (username, passwd) VALUES (?, ?)",
                (username, bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode())
            )
        