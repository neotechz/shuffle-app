from flask import Flask, render_template, redirect, jsonify


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

decks_local = []


# db = SQLAlchemy ?


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/new")
def create_deck():
    # jsonify({})
    redirect("/")


if __name__ == "__main__":
    app.run()