from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", name=None)


@app.route("/<name>")
def hello_world(name):
    return render_template("index.html", name=name)


@app.route("/data", methods=["POST"])
def data():
    name = request.form["name"]
    return render_template("result.html", name=name)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
