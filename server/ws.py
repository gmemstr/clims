from flask import Flask, render_template, request
import mitm as man

app = Flask(__name__, template_folder="../templates/")


@app.route('/')
def Index():
    return render_template("index.html", posts=man.Post())


@app.route('/read/<post>')
def RenderPost(post):
    data = man.Post(post)
    return render_template("post.html", data=data)


@app.route('/new', methods=["PUT"])
def WritePost(type):
    title = request.form["title"]
    text = request.form["text"]
    key = request.form["key"]
    if key == man.Key():
        if title == "" or text == "" or title == None or text == None:
            man.NewPost(title, text)
            return "Posted new blog post"
        else:
            return "No data to post?"

    else:
        return "Invalid or no key"

if __name__ == "__main__":
    app.run(port=8080)
