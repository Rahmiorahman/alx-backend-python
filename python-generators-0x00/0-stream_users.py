import mysql.connector

def stream_users():
    """Yield one user at a time from the user_data table"""
    try:
        # 1. Connect to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",  # replace this
            database="ALX_prodev"
        )

        cursor = connection.cursor(dictionary=True)

        # 2. Run the SQL query
        cursor.execute("SELECT * FROM user_data")

        # 3. Loop through the result using a generator
        for row in cursor:
            yield row  # This returns one row at a time as a dictionary

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
