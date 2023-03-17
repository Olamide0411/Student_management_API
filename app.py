from student_management import create_app
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 


app = create_app()

