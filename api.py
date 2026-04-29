from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the API home"
    
@app.route("/about")
def about():
    return "This is a simple flask app"

@app.route("/contact")
def contact():
    return "Contact me at www.user.com"





    
if __name__ == "__main__":
    app.run(debug =True )


