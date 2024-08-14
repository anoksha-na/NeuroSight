from flask import Flask, render_template
import sqlite3

# Create a Flask app instance
app = Flask(__name__)

# Route to display the contents of the doctors and patients tables
@app.route('/show_users')
def show_users():
    # Connect to the SQLite database
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    
    # Execute a SELECT query to retrieve all records from the doctors table
    c.execute("SELECT * FROM doctors")
    doctors = c.fetchall()
    
    # Execute a SELECT query to retrieve all records from the patients table
    c.execute("SELECT * FROM patients")
    patients = c.fetchall()

    c.execute("SELECT * FROM scans")
    scans = c.fetchall()
    
    # Close the database connection
    conn.close()
    
    # Render a template with the retrieved data
    return render_template('show_users.html', doctors=doctors, patients=patients, scans=scans)

if __name__ == '__main__':
    app.run(debug=True)