from flask import Flask, render_template
import os
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://media.giphy.com/media/kusPzjBcmhc2yB06Tq/giphy.gif"
    ]


@app.route("/")
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)

@app.route("/hello")
def hello():
    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
