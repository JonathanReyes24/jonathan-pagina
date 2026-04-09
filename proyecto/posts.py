from flask import Blueprint, render_template, request

from proyecto.models import Post
from . import db

bpPosts =  Blueprint("posts",__name__)

def reemplazar(texto):
    return texto.replace("January","Enero").replace("enero","Enero").replace("February","Febrero").replace("febrero","Febrero").replace("March","Marzo").replace("marzo","Marzo").replace("April","Abril").replace("abril","Abril").replace("May","Mayo").replace("mayo","Mayo").replace("June","Junio").replace("junio","Junio").replace("July","Julio").replace("julio","Julio").replace("August","Agosto").replace("agosto","Agosto").replace("September","Septiembre").replace("septiembre","Septiembre").replace("October","Octubre").replace("octubre","Octubre").replace("November","Noviembre").replace("noviembre","Noviembre").replace("December","Diciembre").replace("diciembre","Diciembre")

@bpPosts.route("/<url>/")
def post(url):
    post = Post.query.filter_by(url=url).first()
    return render_template("post.html",post=post,reemplazar=reemplazar)

@bpPosts.route("/posts/",methods=["GET","POST"])
def posts():
    posts = Post.query.all()
    if request.method == "POST":
        texto = request.form.get("buscar")
        posts = Post.query.filter(Post.title.ilike(f"%{texto}%")).all()
    return render_template("posts.html",pagina="posts",posts=posts,reemplazar=reemplazar)