from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_bootstrap import Bootstrap
import psycopg2
import hashlib


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random value
bootstrap = Bootstrap(app)


# PostgreSQL Connection
def connect_to_postgres():
    return psycopg2.connect(
        user='postgres',
        password='12345',
        host="localhost",
        dbname='career_portal'
    )


# Function to check if user is logged in
def is_logged_in():
    return 'email' in session


@app.route('/')
def index():
    return render_template('user/index.html', logged_in=is_logged_in())


# Registration route
# Registration route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['name']
        email = request.form['email']
        user_type = request.form['type']
        password = request.form['password']
        hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Hash the password

        if user_type == 'job_seeker':
            type_value = 1
        else:
            type_value = 2

        try:
            conn = connect_to_postgres()
            cursor = conn.cursor()

            # Insert user into the database
            sql = "INSERT INTO users (name, email, type, password) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (username, email, type_value, hashed_password))
            conn.commit()

            flash('Registration successful. Please log in.', 'success')
            if user_type == 'job_seeker':
                return redirect(url_for('profile'))
            elif user_type == 'recruiter':
                return redirect(url_for('jobPost'))
        except psycopg2.Error as e:
            flash('Error registering user. Please try again.', 'danger')
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

    return render_template('user/profile.html')



# Login rout
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Hash the password

        try:
            conn = connect_to_postgres()
            cursor = conn.cursor()

            # Check if the username and password match
            sql = "SELECT * FROM users WHERE email = %s AND password = %s"
            cursor.execute(sql, (email, hashed_password))
            user = cursor.fetchone()

            if user:
                session['email'] = email  # Store the username in the session
                user_type = user[4]
                if user_type == 1:
                    flash('Login successful.', 'success')
                    return redirect(url_for('index'))
                elif user_type == 2:
                    flash('Login successful as recruiter.', 'success')
                    return redirect(url_for('jobPost'))
            else:
                flash('Invalid username or password. Please try again.', 'danger')
                return redirect(url_for('login'))
        except psycopg2.Error as e:
            flash('Error logging in. Please try again.', 'danger')
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

    return render_template('user/index.html')



# Logout route
@app.route('/logout')
def logout():
    session.pop('email', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))


@app.route('/profile')
def profile():
    return render_template('user/profile.html')


# post_a_job route
@app.route('/job-Post', methods=['GET', 'POST'])
def jobPost():
    if request.method == 'POST':
        title = request.form['title']
        organization = request.form['organization']
        location = request.form['location']
        experience = request.form['experience']
        deadline = request.form['deadline']
        category = request.form['category']
        description = request.form['description']

        try:
            conn = connect_to_postgres()
            cursor = conn.cursor()

            # Insert job into the database
            sql = "INSERT INTO jobs (job_title, organization_name, location, work_experience, category , deadline, description) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (title, organization, location, experience, category, deadline, description))
            conn.commit(),

            flash('Job posted successfully.', 'success')
            return redirect(url_for('jobPost'))
        except psycopg2.Error as e:
            flash('Error posting job. Please try again.', 'danger')
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

    return render_template('user/job_post.html')


# post_a_job route
@app.route('/job-list', methods=['GET', 'POST'])
def jobList():
    # Check if 'username' is in session, if not redirect to login
    if 'email' not in session:
        return redirect(url_for('login'))

    # Check if filters are applied
    apply_filters = 'applyFilters' in request.form

    data = []
    try:
        conn = connect_to_postgres()
        cursor = conn.cursor()

        # title = request.form['title']
        # organization = request.form['organization']
        # location = request.form['location']
        # experience = request.form['experience']
        # deadline = request.form['deadline']
        category = request.form.get['category']
        # description = request.form['description']

        # Get search term from form data
        # search_term = request.form.get('applyFilters')

        # Fetch job listings from the database based on search term
        if category:
            sql = "SELECT * FROM jobs WHERE category LIKE %s"
            cursor.execute(sql, ('%' + category + '%',))
        else:
            # If no search term provided, fetch all job listings
            sql = "SELECT job_title,organization_name,location,work_experience,description,deadline FROM jobs"
            cursor.execute(sql)

        # Fetch all rows
        rows = cursor.fetchall()

        # Process the fetched data into a list of dictionaries
        data=[]
        for row in rows:
            data.append({
                "title": row[0],
                "organization": row[1],
                "location": row[2],
                "experience":row[3],
                "description":row[4],
                "deadline":row[5]

            })

    except psycopg2.Error as e:
        flash('An error occurred while fetching data from the database.', 'danger')
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

    # Render the template with the fetched data
    return render_template('user/job_post.html', data=data, apply_filters=apply_filters)

# @app.route('/search', methods=['GET', 'POST'])
# def search():
#     if request.method == 'POST':
#         search_term = request.form['search']
#         try:
#             conn = connect_to_postgres()
#             cursor = conn.cursor()

#             # Search for jobs by title
#             sql = "SELECT * FROM jobs WHERE job_title ILIKE %s"
#             cursor.execute(sql, ('%' + search_term + '%',))
#             jobs = cursor.fetchall()

#             return render_template('index.html', jobs=jobs)

#         except psycopg2.Error as e:
#             flash('Error searching for jobs.', 'danger')
#             print("Error:", e)
#         finally:
#             cursor.close()
#             conn.close()

#     return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)
