import os

from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)


# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine("postgres://ttdyeradcauljg:0c2870d53600062a44fce328cc5b837e60e86f5a1fc1e47a80b63fe1e6eaa505@ec2-3-211-48-92.compute-1.amazonaws.com:5432/d95ge10rl45mqt")
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return "Project 1: TODO"
