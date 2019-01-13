import vk
from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello!"


@app.route('/posts')
def posts():
    limit = request.args.get('limit')
    if limit:
        return jsonify(vk.get_posts(limit))

    return jsonify(vk.get_posts(100))


@app.route('/about')
def about():
    return "about"


@app.route('/post/<int:post_id>')
def post(post_id):
    return jsonify(vk.get_post(post_id))
