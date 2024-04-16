import psycopg2


# def create_database():
#     try:
#         psycopg2_connection = psycopg2.connect(
#             user='postgres',
#             password='12345', 
#             host="localhost",
#             dbname='postgres'
#             )
#         cursor = psycopg2_connection.cursor()
#         cursor.execute("CREATE DATABASE IF NOT EXISTS career_portal")
#         print("Database created successfully.")
#     except psycopg2.Error as err:
#         print(f"Error creating database: {err}")
#     finally:
#         cursor.close()
#         psycopg2_connection.close()



# create_database()

def create_tables():
    try:
        psycopg2_connection = psycopg2.connect(
            user='postgres',
            password='12345', 
            host="localhost",
            dbname='career_portal'
            )
        cursor = psycopg2_connection.cursor()
        # cursor.execute("CREATE TABLE IF NOT EXISTS users (user_id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL UNIQUE, password VARCHAR(255) NOT NULL)")
        cursor.execute("CREATE TABLE IF NOT EXISTS jobs (job_id SERIAL PRIMARY KEY, job_title VARCHAR(255) NOT NULL, organization_name VARCHAR(255) NOT NULL, location VARCHAR(255) NOT NULL, work_experience FLOAT NOT NULL, deadline DATE NOT NULL)")
        psycopg2_connection.commit()
        # print("Table created successfully.")
    except psycopg2.Error as err:
        print(f"Error creating table: {err}")
    finally:
        if cursor:
            cursor.close()
        if psycopg2_connection:
            psycopg2_connection.close()



create_tables()