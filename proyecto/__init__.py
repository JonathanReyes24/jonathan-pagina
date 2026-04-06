from flask import Flask
from flask_mail import Mail

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()   # Se crea una instancia de la base de datos
mail = Mail()

def create_app():
    app = Flask(__name__)

    app.config.from_object("proyecto.config.Config")

    db.init_app(app)
    mail.init_app(app)

    from flask_ckeditor import CKEditor
    ckeditor = CKEditor(app)

    from proyecto.home import bpHome
    app.register_blueprint(bpHome)
    from proyecto.posts import bpPosts
    app.register_blueprint(bpPosts)
    from proyecto.contacto import bpContacto
    app.register_blueprint(bpContacto)
    from proyecto.auth import bpAuth
    app.register_blueprint(bpAuth)

    # from models import Post
    with app.app_context():         
        db.create_all()

    return app