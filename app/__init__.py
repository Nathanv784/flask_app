import os
from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
# from flask_seeder import FlaskSeeder

# Initialize Flask extensions
app = Flask(__name__)
load_dotenv()

# Configure database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# # Initialize FlaskSeeder
# seeder = FlaskSeeder()
# seeder.init_app(app, db)

# Import routes and models after initializing extensions to avoid circular imports
from app import routes 
from app.model import User, Note

# with app.app_context(): #creating the database without any value
#     db.create_all()
#     sample_users = [
#         {"username": "user1","email":"user1@gmail.com"},
#         {"username": "user2","email":"hello@gmail.com"},
#     ]

  
#     for user_data in sample_users:
#         user = User(**user_data)
#         db.session.add(user)

   
#     db.session.commit()
