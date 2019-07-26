from flask import Flask, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True
    

@app.route("/", methods=["GET", "POST"])
def index(): 
    if request.method == "POST":
        username=request.form["username"]
        password=request.form["password"]
        verifypassword=request.form["verifypassword"]
        email=request.form["email"]

        Username_Error=""
        Password_Error=""
        Valid_Error=""
        Email_Error=""

        if len(username)<3 or len(username)>=20:
            Username_Error="Please input valid username."

        if len(password)<3 or len(password)>=20:
            Password_Error="Please input valid password."
        
        elif password!=verifypassword:
            Valid_Error="Passwords doesn't match."
    
        if email:
            if "@" not in email and  "."not in email:
                Email_Error="Email not valid."

        if not Username_Error and not Password_Error and not Valid_Error and not Email_Error:
            return render_template("welcome.html", Username=username, email=email, user_error=Username_Error, password_error=Password_Error, verify_error=Valid_Error, email_error=Email_Error)
        else:
            return render_template("index.html", Username=username, email=email, user_error=Username_Error, password_error=Password_Error, verify_error=Valid_Error, email_error=Email_Error)



    return render_template("index.html")

@app.route("/welcome")
def valid_signup():
    username = request.args.get("username")
    return render_template("welcome.html", username=username)



app.run()




