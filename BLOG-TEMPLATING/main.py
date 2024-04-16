from flask import Flask, render_template
import requests
URL = "https://api.npoint.io/c790b4d5cab58020d391"
app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get(url=URL)
    data_posts = response.json()

    return render_template("index.html",posts=data_posts)

@app.route("/post/<int:id>")

def get_post(id):
    response = requests.get(url=URL)
    data_posts = response.json()
    post = {}
    for new_post in data_posts:
        if new_post["id"] == id:
            post = new_post

    return render_template('post.html',post=post)

if __name__ == "__main__":
    app.run(debug=True)
