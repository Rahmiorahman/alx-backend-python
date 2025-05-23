from datetime import datetime
import functools
import sqlite3

def log_queries():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Assume the first positional argument is the SQL query
            query = args[0] if args else kwargs.get('query', '<no query provided>')
            print(f"[{datetime.now()}] Executing query: {query}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_queries()
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# Example usage
if __name__ == "__main__":
    users = fetch_all_users("SELECT * FROM users")
    for user in users:
        print(user)
