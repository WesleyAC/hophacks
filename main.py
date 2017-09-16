from data import analyze, main
from flask import Flask, session, redirect, url_for, render_template
app = Flask(__name__, static_folder="static")
app.secret_key = "UyeOKsLuiPqBuiY_OgDDc7LuvaTFuvka"

# Loading demo data is slow, so do it on server startup
demodata = analyze.get_demo_data()

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
    global demodata
    if "demo" in session and session["demo"]:
        print(analyze.get_problems(demodata))
    return render_template('trends.html',
            problem1="p1",
            solution1="s1",
            problem2="p2",
            solution2="s2",
            problem3="p3",
            solution3="s3")
