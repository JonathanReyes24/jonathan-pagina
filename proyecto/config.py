import os
class Config:
    DEBUG = False
    SECRET_KEY = os.getenv("SECRET_KEY")   # "b4f1c9e2a7d84c1f93a2e7b6d1c4f8a9e3b7c2d1f4a8b6c3d9e1f2a7c4b8d3e"
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")   # "postgresql+psycopg2://postgres:12345@localhost:5433/posts"
    CKEDITOR_PKG_TYPE="full"
    MAIL_SERVER='sandbox.smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME =   os.getenv("MAIL_USERNAME")  #'ffd4f1068d9775'
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")    #'05499862a98bfa'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

