from flask import Flask, render_template, request
from sql import SqlHandler

sql = SqlHandler()

app = Flask(__name__, template_folder="../templates/")

@app.route('/')
def Index():
    return render_template("index.html", posts=sql.GetPost())

@app.route('/read/<post>')
def RenderPost(post):
    return post

@app.route('/new/<type>', methods=["PUT"])
def WritePost(type):
    title = request.form["title"]
    text = request.form["text"]
    sql.NewPost(title,text)
    return text

if __name__ == "__main__":
    app.run(port=8080)