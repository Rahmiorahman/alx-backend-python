#!/usr/bin/env python3
"""
Query Execution Context Manager
"""

import sqlite3

class ExecuteQuery:
    """
    A context manager that executes a parameterized SQL query and returns results,
    while automatically managing the database connection.
    """
    
    def __init__(self, query, params=None, db_name='users.db'):
        """
        Initialize the context manager with query and parameters
        
        Args:
            query (str): SQL query to execute
            params (tuple): Parameters for the query
            db_name (str): Database file name
        """
        self.query = query
        self.params = params if params is not None else ()
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    def __enter__(self):
        """
        Enter the context - opens connection and executes query
        
        Returns:
            list: Query results
        """
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.query, self.params)
        return self.cursor.fetchall()

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit the context - closes cursor and connection
        """
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        # Return False to propagate any exceptions
        return False


if __name__ == "__main__":
    # Example usage with the specified query
    query = "SELECT * FROM users WHERE age > ?"
    params = (25,)
    
    with ExecuteQuery(query, params) as results:
        print("Users over 25:")
        for row in results:
            print(row)