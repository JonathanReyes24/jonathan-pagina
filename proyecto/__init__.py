from flask import Flask
from flask_mail import Mail
from dotenv import load_dotenv
import os
import cloudinary
import cloudinary.uploader

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()   # Se crea una instancia de la base de datos
mail = Mail()

def create_app():
    app = Flask(__name__)

    load_dotenv()

    app.config.from_object("proyecto.config.Config")

    db.init_app(app)
    mail.init_app(app)

    cloudinary.config(cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),api_key=os.getenv("CLOUDINARY_API_KEY"),api_secret=os.getenv("CLOUDINARY_API_SECRET"),secure=True)

    from flask_ckeditor import CKEditor
    ckeditor = CKEditor(app)

    import locale
    try:
        locale.setlocale(locale.LC_ALL, "es_ES.UTF-8")
    except:
        locale.setlocale(locale.LC_ALL, "")

    from proyecto.home import bpHome
    app.register_blueprint(bpHome)
    from proyecto.posts import bpPosts
    app.register_blueprint(bpPosts)
    from proyecto.contacto import bpContacto
    app.register_blueprint(bpContacto)
    from proyecto.auth import bpAuth
    app.register_blueprint(bpAuth)

    from proyecto.models import Post
    with app.app_context():         
        db.create_all()

    return app