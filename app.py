import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from -- Mohammed Alsailani -- in 3308'


@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://mohammed_db_user:UmSc7JQQWVM3IqL8sbwxtGBI8I4cINRV@dpg-csj5d6btq21c73d9b840-a/mohammed_db")
    conn.close()
    return "Database Connection Successful"