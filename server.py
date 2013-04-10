import codecs
import sh
import os
import json
from sh import pandoc, rm, convert
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/latex", methods=["POST"])
def latex():
    with codecs.open("temp.md", "w+", "utf-8") as f:
        f.write(request.form["content"])
    args = "temp.md --latex-engine=xelatex -t beamer -V theme:Carsurfing -o temp.pdf --smart"
    args = "temp.md --latex-engine=xelatex -t beamer -o temp.pdf --smart"
    pandoc_status = pandoc(*args.split(" "))

    rm_status = rm(sh.glob("static/images/*"), "-r")

    args = "-quality 100 -density 200x200 temp.pdf static/images/output%d.jpg"
    convert_status = convert(*args.split(" "))

    image_dir = "static/images"
    files = os.listdir(image_dir)

    print pandoc_status, rm_status, convert_status

    return json.dumps(files)

app.run(debug=True, host='0.0.0.0')