
from flask import Flask,render_template,request

import os

import main

app=Flask(__name__)

app.secret_key='dbhjsiuyf'

s=main.Scrap()

@app.route('/')
def home():

    return render_template('index.html')

@app.route('/scrap',methods=['GET','POST'])
def scrap():

    Query=request.form.get('content')

    Response=s.Scraper(Query)

    return render_template('index.html',Response=Response)



if __name__ =="__main__":
    print("Starting Flask app on http://127.0.0.1:5000")
    app.run(debug=True, host='127.0.0.1', port=5000)
    app.run(debug=True)