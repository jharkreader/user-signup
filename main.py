#!/usr/bin/env python

__author__ = "student"
__version__ = "1.0"
# June 2017
# Flask User Sign-up web app
# LC-101 Project Rubric: http://education.launchcode.org/web-fundamentals/assignments/user-signup/


from flask import Flask, request, redirect, render_template
import re

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/", methods=["GET", "POST"])
def index():
    title = 'User login'
    username = ''
    email = ''
    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        verify_password = request.form['v_password']
        email = request.form['email']

        if username == "":
            username_error = "Please enter a username."
        elif (len(username) <= 3) or (len(username) >= 20):
            username_error = "User name must be greater than 3 but less than 20 characters."
        elif " " in username:
            username_error = "User name cannot contain spaces."
        else:
            pass

        if password == "":
            password_error = "Please enter a password."
        elif (len(password) <= 3) or (len(password) >= 20):
            password_error = "Password must be greater than 3 but less than 20 characters."
        elif " " in password:
            password_error = "Password cannot contain spaces."
        elif password != verify_password:
            verify_password_error = "Passwords must match."
            password_error = "Passwords must match."
        else:
            pass

        if (email != "") and (not re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email)):
                email_error = "Please enter a valid email address."
                email = ""

        if (not username_error) and (not password_error) and (not verify_password_error) and (not email_error):
            return redirect('/valid-signup?username={0}'.format(username))

    return render_template('login_form.html', title=title, username_error=username_error, password_error=password_error,
                           verify_password_error=verify_password_error, email_error=email_error, username=username,
                           email=email)


@app.route("/valid-signup")
def send():
    title = "welcome"
    username = request.args.get("username")
    return render_template('welcome.html', title=title, username=username)


if __name__ == '__main__':
    app.run()
