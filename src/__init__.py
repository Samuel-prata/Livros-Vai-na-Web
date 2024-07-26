from flask import Flask
from config import Config
from .blueprint.routes import livro_bp
from .model import database


def create_app():
    app = Flask(__name__)
    #Seta o arquivo de configurações
    app.config.from_object(Config)
    app.register_blueprint(livro_bp)
    #Vinculando o SQLAlchemy com o Flask
    database.init_app(app)


    with app.app_context():
        from .blueprint import routes
        # Criação de todas as tabelas definidas no arquivo models.py
        database.create_all()
    return app