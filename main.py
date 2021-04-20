from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON
import os
import json

app = Flask(__name__)

HOST = os.environ.get('POSTGRES_URL')
NAME = os.environ.get('POSTGRES_DB')
USER = os.environ.get('POSTGRES_USER')
PASSWORD = os.environ.get('POSTGRES_PW')

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}/{NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class Example(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    json_column = db.Column(JSON)

def insert_data():
    with open ("data.json") as file:
        data = json.load(file)
    example1 = Example(json_column={"key" : "value", "myarray" : [39, 323, 83, 382, 102], "objects" : {"name" : "Anthony"}})
    example2 = Example(json_column={"key" : "newvalue", "myarray" : [23, 676, 45, 88, 99], "objects" : {"name" : "Brian"}})
    example3 = Example(json_column=data)
    db.session.add(example1)
    db.session.add(example2)
    db.session.add(example3)
    db.session.commit()

def query():
    example1 = Example.query.first()
    print(example1.json_column)
    print('\n\n\n\n')

    results = Example.query.filter(Example.json_column['objects']['name'].astext == 'Brian').all()
    for result in results:
        print(result.json_column)
    print('\n\n\n\n')

    results = Example.query.all()
    for result in results:
        print(result.json_column)


db.create_all()
insert_data()
query()
