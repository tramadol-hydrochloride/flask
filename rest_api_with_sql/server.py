from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager
from flask_cors import CORS


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/nobel_prize.db'
app.config['CORS_ALLOW_HEADERS'] = 'Content-Type'
app.config['CORS_RESOURCES'] = {r'/api/*': {'origins': '*'}}

db = SQLAlchemy(app)
cors = CORS(app)


class Winners(db.Model):
    __tablename__ = 'winners'
    index = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)
    category = db.Column(db.Unicode)
    year = db.Column(db.Unicode)
    country = db.Column(db.Unicode)
    gender = db.Column(db.Unicode)


db.create_all()

manager = APIManager(app, flask_sqlalchemy_db=db)

manager.create_api(Winners,
                   methods=['GET'],
                   max_results_per_page=1000)

app.run()
