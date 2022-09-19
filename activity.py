from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)  

@app.route('/')
@app.route('/home')  
def home():  
    return render_template("index.html")
@app.route("/login", methods=["GET", "POST"]) 
def login():
    if request.method == "POST":
        name = request.form["names"]
        return redirect(url_for("name", name=name))
    else:
        return render_template("index.html")
    

    
@app.route("/good", methods=["GET", "POST"]) 
def good():
    if request.method == "POST":
        characs = request.form["charac"]
        return redirect(url_for("characs", characs=characs))
    else:
        return render_template("index.html")
 
# @app.route("/<usr>") 
# def user(usr): 
#     return f"<h1>{usr}</h1>"  
    
if __name__ =="__main__":  
    app.run(debug = True)  