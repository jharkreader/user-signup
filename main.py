from flask import Flask, request, redirect, render_template, send_from_directory
import cgi

app = Flask(__name__, static_url_path='/static')
app.config['DEBUG'] = True 


@app.route("/")
def index():

    return render_template('index.html')

@app.route("/send", methods=["POST"])
def send():
    username = request.form["username"]
    return render_template('welcome.html', username=username)

@app.route('/static')
def send_css(/static):
    return send_from_directory('stylesheet.css', /static)

app.run()    