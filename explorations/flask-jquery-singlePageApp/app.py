from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = "Paul"
    return(render_template("test.html", title=name))

@app.route("/data")
def data():
    profile = {
        "name": "Paul",
        "badges": ["one", "two", "three"]
        };
    return(jsonify(profile));


if __name__ == '__main__':
   app.run(debug=True)


