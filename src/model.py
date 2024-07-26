from flask_sqlalchemy import SQLAlchemy
database = SQLAlchemy()

class Livro(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String(100), nullable=False)
    autor = database.Column(database.String(100), nullable=False)
    paginas = database.Column(database.Integer)
    disponivel = database.Column(database.Boolean)

    def __init__(self, titulo, autor, paginas, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponivel = disponivel

    def to_dict(self):
        return {
            'titulo': self.titulo,
            'autor': self.autor,
            'isdisp': self.disponivel
        }

