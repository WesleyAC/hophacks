from data import analyze
from flask import Flask, session, redirect, url_for, render_template
app = Flask(__name__, static_folder="static")
app.secret_key = "UyeOKsLuiPqBuiY_OgDDc7LuvaTFuvka"

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/login')
def login():
    return app.send_static_file('login.html')

@app.route('/demo')
def demo():
    session['demo'] = True
    return redirect(url_for('trends'))

@app.route("/trends")
def trends():
    return render_template('trends.html')
