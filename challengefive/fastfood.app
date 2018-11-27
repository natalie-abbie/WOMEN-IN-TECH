from flask import Flask, render_template, redirect, url_for, request, session, flash

app = Flask(__name__)

app.secret_key = "natalie123"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/welcome')
def Welcome():
    return render_template("welcome.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == ' POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials. please try again.'
    else:
