from core import app
from flask import render_template


@app.route("/")
def index():
    context = {
        'title': 'Flask Complaints Board',
    }
    return render_template("index.html", context=context)
