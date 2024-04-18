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
        # cursor.execute("CREATE TABLE IF NOT EXISTS jobs (job_id SERIAL PRIMARY KEY, job_title VARCHAR(255) NOT NULL, organization_name VARCHAR(255) NOT NULL, location VARCHAR(255) NOT NULL, work_experience FLOAT NOT NULL, deadline DATE NOT NULL)")
        #         cursor.execute("""
        #     CREATE TABLE IF NOT EXISTS personal_details (
        #     id SERIAL PRIMARY KEY,
        #     photo BYTEA,
        #     first_name VARCHAR(100),
        #     last_name VARCHAR(100),
        #     father_name VARCHAR(100),
        #     mother_name VARCHAR(100),
        #     gender VARCHAR(10),
        #     religion VARCHAR(50),
        #     marital_status VARCHAR(20),
        #     nationality VARCHAR(50),
        #     national_id VARCHAR(50),
        #     primary_mobile VARCHAR(20),
        #     secondary_mobile VARCHAR(20),
        #     primary_email VARCHAR(100),
        #     blood_group VARCHAR(10),
        #     alternate_email VARCHAR(100),
        #     present_country VARCHAR(100),
        #     present_district VARCHAR(100),
        #     present_thana VARCHAR(100),
        #     present_zip_code VARCHAR(20),
        #     present_house_no VARCHAR(100),
        #     permanent_country VARCHAR(100),
        #     permanent_district VARCHAR(100),
        #     permanent_thana VARCHAR(100),
        #     permanent_zip_code VARCHAR(20),
        #     permanent_house_no VARCHAR(100),
        #     user_id INT,
        #     FOREIGN KEY (user_id) REFERENCES users(user_id)
        #     );
        # )

        # cursor.execute("""
        #     CREATE TABLE IF NOT EXISTS education (
        #         id SERIAL PRIMARY KEY,
        #         academic_level VARCHAR(100),
        #         exam_title VARCHAR(255),
        #         major VARCHAR(255),
        #         institute_name VARCHAR(255),
        #         result_type VARCHAR(50),
        #         result_value FLOAT,
        #         passing_year INT,
        #         achievement TEXT,
        #         training_title VARCHAR(255),
        #         training_country VARCHAR(100),
        #         training_year INT,
        #         training_institute VARCHAR(255),
        #         training_start_date DATE,
        #         training_end_date DATE,
        #         training_location VARCHAR(255),
        #         user_id INT,
        #         FOREIGN KEY (user_id) REFERENCES users(user_id)
        #     );
        # """)

        #         cursor.execute("""
        #     CREATE TABLE IF NOT EXISTS employment_history (
        #         id SERIAL PRIMARY KEY,
        #         company_name VARCHAR(255),
        #         designation VARCHAR(255),
        #         department VARCHAR(255),
        #         start_date DATE,
        #         end_date DATE,
        #         responsibilities TEXT,
        #         expertise VARCHAR(255),
        #         location VARCHAR(255),
        #         user_id INT,
        #         FOREIGN KEY (user_id) REFERENCES users(user_id)
        #     );
        # """)


        # cursor.execute("""
        #     CREATE TABLE IF NOT EXISTS other_info (
        #         id SERIAL PRIMARY KEY,
        #         skill VARCHAR(255),
        #         user_id INT,
        #         FOREIGN KEY (user_id) REFERENCES users(user_id)
        #     );
        # """)


        # cursor.execute("""

        #     CREATE TABLE IF NOT EXISTS accomplishment (
        #         id SERIAL PRIMARY KEY,
        #         user_id INT,
        #         portfolio_title VARCHAR(255),
        #         portfolio_description TEXT,
        #         portfolio_link VARCHAR(255),
        #         publication_title VARCHAR(255),
        #         publication_description TEXT,
        #         publication_link VARCHAR(255),
        #         project_title VARCHAR(255),
        #         project_description TEXT,
        #         project_link VARCHAR(255),
        #         FOREIGN KEY (user_id) REFERENCES users(user_id)
        #     );

        #     """)


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