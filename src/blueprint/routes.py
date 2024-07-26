from flask import request, jsonify, Blueprint
from ..model import database
from ..model import Livro

livro_bp = Blueprint('livros', __name__)


@livro_bp.route('/doar_livro', methods=['POST', ])
def doar_livro():
    dados = request.get_json()
    titulo = dados.get('titulo')
    autor = dados.get('autor')
    paginas = dados.get('paginas')
    print(f'{type(paginas)}')
    livro = Livro(titulo, autor, paginas)
    database.session.add(livro)
    database.session.commit()
    return 'Sucesso'

@livro_bp.route('/livros')
def pegar_livros():
    livros = Livro.query.all()
    livros_dict = [livro.to_dict() for livro in livros]
    return jsonify(livros_dict)