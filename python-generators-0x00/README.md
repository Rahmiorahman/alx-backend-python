# 0x00. Python - Generators

## Description

This project demonstrates how to set up a MySQL database and stream data using Python generators.

- It creates a database called `ALX_prodev`.
- It creates a table `user_data` with the following columns:
  - `user_id` (UUID, primary key)
  - `name` (text)
  - `email` (text)
  - `age` (number)
- It reads and inserts data from a CSV file `user_data.csv`.
- It includes a generator that streams rows from the table one at a time.

## Files

- `seed.py`: Main script that connects to MySQL, creates the database/table, inserts data, and includes the generator.
- `0-main.py`: Test file that runs the setup and shows how to use the generator.
- `user_data.csv`: Sample CSV file with user data.
- `README.md`: Project documentation (this file).

## Requirements

- Python 3.6 or higher
- `mysql-connector-python` library
- MySQL server installed and running

## Setup Instructions

1. Install MySQL and create a user with access.
2. Install the required Python package:

   ```bash
   pip install mysql-connector-python
b