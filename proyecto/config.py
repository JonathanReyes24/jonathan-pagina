import os
class Config:
    DEBUG = False
    SECRET_KEY = os.environ.get("SECRET_KEY","dev")   # "b4f1c9e2a7d84c1f93a2e7b6d1c4f8a9e3b7c2d1f4a8b6c3d9e1f2a7c4b8d3e"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")   # "postgresql+psycopg2://postgres:12345@localhost:5433/posts"
    CKEDITOR_PKG_TYPE="full"
    MAIL_SERVER='sandbox.smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME =   os.environ.get("MAIL_USERNAME")  #'ffd4f1068d9775'
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")    #'05499862a98bfa'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

