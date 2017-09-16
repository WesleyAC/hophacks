from data import analyze, main
from data.tidepool_import import tidepool_import
import uuid
import json
from flask import Flask, Response, session, request, redirect, url_for, render_template
app = Flask(__name__, static_folder="static")
app.secret_key = "UyeOKsLuiPqBuiY_OgDDc7LuvaTFuvka"

# Loading demo data is slow, so do it on server startup
#TODO(Wesley) add more demos users
data = {"demo": analyze.demo_data_a}


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

@app.route('/demo', methods=["POST"])
def demo_post():
    session['id'] = request.form["demo_user"]
    return Response("OK", status=200)

@app.route('/demo', methods=["GET"])
def demo():
    # return app.send_static_file('demo.html')
    session['id'] = 'demo'
    return redirect(url_for("trends"))

@app.route('/graph')
def graph():
    return Response(json.dumps([{"date": "[{:02d},{:02d}]".format(k.hour, k.minute), "bg": v} for (k,v) in sorted(data[session["id"]].avgs.items())]), mimetype="application/json")

@app.route("/trends")
def trends():
    global demodata
    problems = []
    settings = None
    if "id" in session:
        for problem in analyze.get_problems(data[session["id"]]):
            problems.append(analyze.problem_to_text(problem))
        settings = analyze.get_schedule(data[session["id"]])
        new_settings = analyze.get_new_schedule(data[session["id"]])
    else:
        return redirect(url_for("login_get"))

    mapping = ['#one!','#two!','#three!','#four!','#five!','#six!']
    return render_template('trends.html', problems=problems, settings=settings, new_settings=new_settings, mapping=mapping)
