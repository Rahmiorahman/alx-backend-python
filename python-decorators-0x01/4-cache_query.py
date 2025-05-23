import sqlite3
import functools

# Global dictionary to store cached queries
query_cache = {}

def with_db_connection(func):
    """Decorator to manage database connections"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            result = func(conn, *args, **kwargs)
            return result
        finally:
            conn.close()
    return wrapper

def cache_query(func):
    """Decorator to cache database query results"""
    @functools.wraps(func)
    def wrapper(conn, query, *args, **kwargs):
        # Check if query is already cached
        if query in query_cache:
            print("Using cached result for query:", query)
            return query_cache[query]
            
        # Execute and cache if not found
        result = func(conn, query, *args, **kwargs)
        query_cache[query] = result
        print("Caching new result for query:", query)
        return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    """Fetch users with query caching"""
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# First call will execute and cache
print("First call (executes query):")
users = fetch_users_with_cache(query="SELECT * FROM users")

# Second call will use cache
print("\nSecond call (uses cache):")
users_again = fetch_users_with_cache(query="SELECT * FROM users")