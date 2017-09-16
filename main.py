from data import analyze, main
from data.tidepool_import import tidepool_import
import uuid
from flask import Flask, Response, session, request, redirect, url_for, render_template
app = Flask(__name__, static_folder="static")
app.secret_key = "UyeOKsLuiPqBuiY_OgDDc7LuvaTFuvka"

# Loading demo data is slow, so do it on server startup
demodata = analyze.get_demo_data()
data = {"demo": demodata}


@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/login', methods=["GET"])
def login_get():
    return app.send_static_file('login.html')

@app.route('/login', methods=["POST"])
def login_post():
    global data
    sid = uuid.uuid4().hex
    session["id"] = sid
    data[sid] = tidepool_import(request.form["username"], request.form["password"])
    return Response("OK", status=200) #TODO(Wesley) fail

@app.route('/demo')
def demo():
    session['id'] = "demo"
    return redirect(url_for('trends'))

@app.route("/trends")
def trends():
    global demodata
    problems = []
    if "id" in session:
        for problem in analyze.get_problems(data[session["id"]]):
            problems.append(analyze.problem_to_text(problem))
    else:
        return redirect(url_for("login_get"))

    return render_template('trends.html', problems=problems)
