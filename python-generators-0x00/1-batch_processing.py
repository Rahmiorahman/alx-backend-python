import mysql.connector

# Generator to fetch rows in batches
def stream_users_in_batches(batch_size):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",  # Replace with your MySQL password
        database="ALX_prodev"
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    while True:
        batch = cursor.fetchmany(batch_size)
        if not batch:
            break
        yield batch

    cursor.close()
    conn.close()

# Function to process each batch and filter users over 25
def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)
