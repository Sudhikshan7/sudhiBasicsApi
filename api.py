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

@app.route("/hello", methods=["POST"])
def hello():
    data = request.form.get("name")
    if not data:
        return "No name provided in POST REQUEST", 400
    return f"Hello, {data.capitalize()}! Heyy cham how are you doing??"


    
if __name__ == "__main__":
    app.run(debug =True )


