from flask import Blueprint, render_template, request, session, url_for, redirect, g, flash

bpAuth =  Blueprint("auth",__name__,url_prefix="/h20f24")
from proyecto.models import Post
from . import db

@bpAuth.before_app_request
def load_logged_in_user():
    usuario = session.get("usuario")
    if usuario == None:
        g.user = None
    else:                  
        g.user = "Jonathan"

import functools
def login_required(vista):
    @functools.wraps(vista)
    def vista_envuelta(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))
        return vista(**kwargs)
    return vista_envuelta

def login_accepted(vista):
    @functools.wraps(vista)
    def vista_envuelta(**kwargs):
        if g.user is not None:
            return redirect(url_for("auth.admin"))
        return vista(**kwargs)
    return vista_envuelta

@bpAuth.route("/login", methods=("GET","POST"))
@login_accepted
def login():
    if request.method == "POST":
        usuario = request.form.get("usuario")
        contraseña = request.form.get("contraseña")

        error = None
        if usuario == "Jonathan24__" and contraseña =="Laberinto_mph24@":
            session.clear()
            session["usuario"] = "Jonathan"
            return redirect(url_for('auth.admin'))
        else:
            error = "Datos de ingreso incorrectos"
            flash(error)
    return render_template("auth/login.html")

@bpAuth.route("/logout")
@login_required
def logout():
    session.clear()
    return redirect(url_for("auth.login"))

@bpAuth.route("/admin")
@login_required
def admin():
    return render_template("auth/admin.html")

@bpAuth.route("/posts")
@login_required
def posts():
    posts = Post.query.all() 
    return render_template("auth/posts.html",posts=posts)

from werkzeug.utils import secure_filename

@bpAuth.route("/post/<accion>/<int:id>",methods=("GET","POST"))
@login_required
def post(accion,id):
    if accion == "publicar":
        post=None
        if request.method == "POST":
            titulo = request.form.get("titulo")
            url = titulo.replace(" ","-").lower()
            info = request.form.get("info")
            contenido = request.form.get("ckeditor")
            photo = request.files["photo"]
            photo.save(f"static/media/{secure_filename(photo.filename)}")
            photo = f"media/{secure_filename(photo.filename)}"

            post_url = Post.query.filter_by(url=url).first()
            if post_url == None:
                post = Post(titulo,url,info,contenido,photo)
                db.session.add(post)
                db.session.commit()
                return redirect(url_for('auth.posts'))
    
    if accion == "editar":
        post = Post.query.get_or_404(id)
        if request.method == "POST":
            post.title = request.form.get("titulo")
            post.url = request.form.get("titulo").replace(" ","-").lower()
            post.info = request.form.get("info")
            post.content = request.form.get("ckeditor")
            if request.files["photo"]:
                photo = request.files["photo"]
                photo.save(f"static/media/{secure_filename(photo.filename)}")
                post.photo = f"media/{secure_filename(photo.filename)}"
            else:
                post.photo = post.photo
            db.session.commit()
            return redirect(url_for('auth.posts'))

    if accion == "eliminar":
        post = Post.query.get_or_404(id)
        db.session.delete(post)
        db.session.commit()
        return redirect(url_for('auth.posts'))
    return render_template("auth/post.html",accion=accion,post=post)


