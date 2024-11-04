## Mohammed Alsailani
## 11/3/2024
## CSPB 3308 - Lab 10 
###############################################################################
## This is for testing deployment of website using Flask
##
###############################################################################

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


@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgresql://mohammed_db_user:UmSc7JQQWVM3IqL8sbwxtGBI8I4cINRV@dpg-csj5d6btq21c73d9b840-a/mohammed_db")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball (
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
        );
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"


@app.route('/db_insert')
def inserting():
    conn = psycopg2.connect("postgresql://mohammed_db_user:UmSc7JQQWVM3IqL8sbwxtGBI8I4cINRV@dpg-csj5d6btq21c73d9b840-a/mohammed_db")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        VALUES
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated"



@app.route('/db_select')
def selecting():
    conn = psycopg2.connect("postgresql://mohammed_db_user:UmSc7JQQWVM3IqL8sbwxtGBI8I4cINRV@dpg-csj5d6btq21c73d9b840-a/mohammed_db")
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM Basketball;
    ''')
    records = cur.fetchall()
    conn.close()
    
    response_string = ""
    response_string += "<table>"
    for player in records:
        response_string += "<tr>"
        for info in player:
            response_string += "<td>{}</td>".format(info)
        response_string += "</tr>"
    response_string += "</table>"
    
    return response_string


@app.route('/db_drop')
def dropping():
    conn = psycopg2.connect("postgresql://mohammed_db_user:UmSc7JQQWVM3IqL8sbwxtGBI8I4cINRV@dpg-csj5d6btq21c73d9b840-a/mohammed_db")
    cur = conn.cursor()
    cur.execute('''
        DROP TABLE Basketball;
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Dropped"
