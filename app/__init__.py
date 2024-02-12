from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from db import db
from dotenv import load_dotenv
import os
load_dotenv()
db_pass=os.getenv("DB_PASS")
db_username=os.getenv("DB_USERNAME")
db_database=os.getenv("DB_DATABASE")
print(os.getenv("DATABASE_URL"))
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB_URI") #config with the pgadmin database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Initialize SQLAlchemy with the Flask app
#db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)

from app.model import User , Note