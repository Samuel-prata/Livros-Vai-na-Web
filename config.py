import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://{nome_usuario}:{senha}@localhost/{banco_de_dados}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY= os.urandom(24)