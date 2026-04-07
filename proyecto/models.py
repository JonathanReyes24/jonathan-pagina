from . import db

from datetime import datetime   # Del módulo "datetime" se importa la función "datetime" para trabajar con fechas
class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),nullable=False,unique=True)
    url = db.Column(db.String(100),nullable=False,unique=True)
    info = db.Column(db.Text)
    content = db.Column(db.Text)
    created = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)    # El tipo de dato es fecha (db.DateTime) y con su valor por default de la fecha en que se publica "datetime.utcnow"
    photo = db.Column(db.Text,nullable=False)

    def __init__(self,title,url,info,content,photo):
        self.title = title
        self.url = url
        self.info = info
        self.content = content
        self.photo = photo

    def __repr__(self):
        return f"Post: '{self.title}'"