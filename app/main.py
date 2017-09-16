from flask import Flask, render_template
app = Flask(__name__, static_folder="static")

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/login')
def login():
    return app.send_static_file('login.html')

@app.route("/trends")
def trends():
    return render_template('trends.html')
