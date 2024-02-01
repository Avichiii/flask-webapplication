from flask import Flask

app = Flask(__name__)

@app.route("/")
def helloWorld():
    return "hello world"

@app.route("/login")
def login():
    return "no login option is available at the moment!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)