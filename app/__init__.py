import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_seeder import FlaskSeeder

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Configure database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)
from app import routes 

