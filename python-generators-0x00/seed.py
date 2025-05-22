#!/usr/bin/env python3
import mysql.connector
from mysql.connector import errorcode
import csv

DB_NAME = "ALX_prodev"

def connect_db():
    """Connects to MySQL server (no specific database yet)"""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"  # 🔁 Change to your MySQL root password
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None

def create_database(connection):
    """Creates ALX_prodev database if it doesn't exist"""
    try:
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        cursor.close()
        print("Database created or already exists.")
    except mysql.connector.Error as err:
        print(f"Error creating database: {err}")

def connect_to_prodev():
    """Connects directly to ALX_prodev database"""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",  # 🔁 Change to your MySQL root password
            database=DB_NAME
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to ALX_prodev: {err}")
        return None

def create_table(connection):
    """Creates user_data table with the specified fields"""
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                user_id VARCHAR(36) NOT NULL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL(10, 0) NOT NULL,
                INDEX(user_id)
            )
        """)
        cursor.close()
        print("Table user_data created successfully.")
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")

def insert_data(connection, filename):
    """Inserts user data from a CSV file into the user_data table"""
    try:
        cursor = connection.cursor()
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cursor.execute("""
                    INSERT IGNORE INTO user_data (user_id, name, email, age)
                    VALUES (%s, %s, %s, %s)
                """, (row['user_id'], row['name'], row['email'], row['age']))
        connection.commit()
        cursor.close()
        print("Data inserted successfully.")
    except FileNotFoundError:
        print(f"CSV file '{filename}' not found.")
    except mysql.connector.Error as err:
        print(f"MySQL error: {err}")

def stream_user_data(connection):
    """Generator that yields one row at a time from user_data"""
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data")
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        yield row
    cursor.close()
