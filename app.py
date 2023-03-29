from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O poder da ação',
        'autor': 'Paulo Viera',
    },
    {
        'id': 2,
        'titulo': 'O poder da ação',
        'autor': 'Paulo Viera',
    },
    {
        'id': 3,
        'titulo': 'O poder da ação',
        'autor': 'Paulo Viera',
    }
]

# Obter todos
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

# Obter por id
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

# Editar por id
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

# Incluir novo livro
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return {'mensagem': 'Livro criado com sucesso!'}, 201

# Exluir livro por id
@app.route('/livros/<int:id>', methods=['DELETE'])
def exluir_livro_por_id(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]      
    return {'mensagem': 'Livro exluído com sucesso!'}, 200
    

app.run(port=5000, host='localhost', debug=True)
