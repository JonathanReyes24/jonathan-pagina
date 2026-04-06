from flask import Blueprint, render_template, request

from proyecto.models import Post
from . import db

bpPosts =  Blueprint("posts",__name__)

@bpPosts.route("/<url>/")
def post(url):
    post = Post.query.filter_by(url=url).first()
    return render_template("post.html",post=post)

@bpPosts.route("/posts/",methods=["GET","POST"])
def posts():
    posts = Post.query.all()
    if request.method == "POST":
        texto = request.form.get("buscar")
        posts = Post.query.filter(Post.title.ilike(f"%{texto}%")).all()
    return render_template("posts.html",pagina="posts",posts=posts)