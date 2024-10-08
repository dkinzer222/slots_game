from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the MySQL database connection using SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlclient://dkinzer222:Adverse2024%21@dkinzer222.mysql.pythonanywhere-services.com/dkinzer222$default'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable warning for unnecessary tracking modifications

# Initialize the database with SQLAlchemy
db = SQLAlchemy(app)

# Define a simple User model (you can modify this based on your needs)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Route for testing if the app is running
@app.route('/')
def index():
    return "Flask App connected to MySQL Database!"

# Route for adding a new user (for testing)
@app.route('/add_user/<username>/<email>')
def add_user(username, email):
    try:
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        return f"Added user {username} to the database!"
    except Exception as e:
        db.session.rollback()
        return f"Failed to add user: {str(e)}"

# Route for displaying all users in the database (for testing)
@app.route('/users')
def get_users():
    try:
        users = User.query.all()
        return '<br>'.join([f'ID: {user.id}, Username: {user.username}, Email: {user.email}' for user in users])
    except Exception as e:
        return f"Failed to fetch users: {str(e)}"

# Add the dummy user directly for testing
@app.route('/add_dummy_data')
def add_dummy_data():
    return add_user('brittbritt', 'brittbritta@gmail.com')

# Run the app
if __name__ == '__main__':
    app.run()
