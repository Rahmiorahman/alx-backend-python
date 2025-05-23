#!/usr/bin/env python3
"""
Concurrent Asynchronous Database Queries
"""

import asyncio
import aiosqlite

async def async_fetch_users(db_path='users.db'):
    """
    Fetch all users from the database asynchronously
    
    Returns:
        list: All users in the database
    """
    async with aiosqlite.connect(db_path) as db:
        async with db.execute("SELECT * FROM users") as cursor:
            return await cursor.fetchall()

async def async_fetch_older_users(db_path='users.db'):
    """
    Fetch users older than 40 asynchronously
    
    Returns:
        list: Users older than 40
    """
    async with aiosqlite.connect(db_path) as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            return await cursor.fetchall()

async def fetch_concurrently():
    """
    Execute both queries concurrently using asyncio.gather
    """
    return await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )

def print_results(all_users, older_users):
    """
    Print the query results in a readable format
    """
    print("\nAll Users:")
    for user in all_users:
        print(user)
    
    print("\nUsers Older Than 40:")
    for user in older_users:
        print(user)

if __name__ == "__main__":
    # Run the concurrent queries
    all_users, older_users = asyncio.run(fetch_concurrently())
    
    # Display results
    print_results(all_users, older_users)