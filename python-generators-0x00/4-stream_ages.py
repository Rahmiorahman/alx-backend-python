#!/usr/bin/python3
seed = __import__('seed')


def stream_user_ages():
    """Generator that yields ages from the user_data table one by one."""
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data")
    for row in cursor:
        yield row["age"]
    connection.close()


def compute_average_age():
    """Computes the average age using the age generator."""
    total_age = 0
    count = 0
    for age in stream_user_ages():
        total_age += age
        count += 1
    if count == 0:
        print("No users found.")
    else:
        average = total_age / count
        print(f"Average age of users: {average:.2f}")


# Run only if this file is executed directly
if __name__ == "__main__":
    compute_average_age()
