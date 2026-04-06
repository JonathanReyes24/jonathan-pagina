from flask import Blueprint, render_template

bpHome =  Blueprint("home",__name__)
from proyecto.models import Post
from . import db

@bpHome.route("/")
def index():
    posts = Post.query.order_by(Post.id.desc()).limit(5).all()
    return render_template("index.html",posts=posts)