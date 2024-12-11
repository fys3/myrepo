import json
from random import choice
from pathlib import Path

from flask import Flask, render_template

app = Flask(__name__)

with open(Path(__file__).parent / "text.json", "r", encoding="utf-8") as f:
    quotes = json.load(f)


@app.route("/")
def home():
    image_url = "https://platform.polygon.com/wp-content/uploads/sites/2/chorus/uploads/chorus_asset/file/24458108/captain_pikachu.jpg?quality=90&strip=all&crop=7.8125%2C0%2C84.375%2C100&w=750"
    repo_url = "https://github.com/eugenegoh92/myrepo"
    quote = choice(quotes)

    return render_template(
        "index.html", image_url=image_url, repo_url=repo_url, quote=quote
    )


if __name__ == "__main__":
    app.run(debug=True)
