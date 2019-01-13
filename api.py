import vk
from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello!"


@app.route('/posts')
def posts():
    return jsonify(vk.get_posts())


@app.route('/about')
def about():
    return "about"


@app.route('/post/<int:post_id>')
def post(post_id):
    return jsonify(vk.get_post(post_id))
