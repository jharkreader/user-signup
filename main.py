from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True 


@app.route("/")
def index():

    return render_template('index.html')


@app.route("/", methods=["POST"])
def validate_signup():
    username = request.form['username']
    pw = request.form['password']
    v_pw = request.form['v_password']
    email = request.form['email']

    username_error = ''
    pw_error = ''
    v_pw_error = ''
    email_error = ''

    if username == "":
        username_error = "Please enter a username."
    elif len(username) < 3 or len(username) > 20:
        username_error = "User name must be greater than 3 but less than 20 characters."
    elif " " in username:
        username_error = "User name cannot contain spaces."
    else:
        pass        

    if pw == "":
        pw_error = "Please enter a password."
    elif len(pw) < 3 or len(pw) > 20:
        pw_error = "Password must be greater than 3 but less than 20 characters."
        pw = ""
        v_pw = ""
    elif " " in pw:
        pw_error = "Password cannot contain spaces."
        pw = ""
        v_pw = ""
    elif pw != v_pw:
        v_pw_error = "Passwords must match."
        pw_error = "Passwords must match."
        v_pw = ""
        pw = ""    
    else:
        pass        

    if email != "":
        if "@" not in email or "." not in email or len(email) < 3 or len(email) > 20 or " " in email:
            email_error = "Please enter a valid email address."
    else:
        pass


    if not username_error and not pw_error and not v_pw_error and not email_error:
        return redirect('/valid-signup?username={0}'.format(username))

    else:
        return render_template('index.html', 
        username_error=username_error, 
        pw_error=pw_error, 
        v_pw_error=v_pw_error, 
        email_error=email_error, 
        username=username, 
        email=email)    


@app.route("/valid-signup")
def send():
    username = request.args.get("username")
    return render_template('welcome.html', username=username)


app.run()    