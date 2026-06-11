from flask import Flask, render_template
from datos import cantantes

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", cantantes=cantantes.keys())


if __name__ == "__main__":
    app.run(debug=True)
