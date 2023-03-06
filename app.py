from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///funcionarios.db'
db = SQLAlchemy(app)

class Funcionario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    cargo = db.Column(db.String(50))
    salario = db.Column(db.Float)

    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

@app.route('/funcionarios', methods=['GET'])
def get_funcionarios():
    funcionarios = Funcionario.query.all()
    output = []
    for funcionario in funcionarios:
        output.append({'id': funcionario.id, 'nome': funcionario.nome, 'cargo': funcionario.cargo, 'salario': funcionario.salario})
    return jsonify({'funcionarios': output})

@app.route('/funcionarios/<id>', methods=['GET'])
def get_funcionario(id):
    funcionario = Funcionario.query.filter_by(id=id).first()
    if not funcionario:
        return jsonify({'message': 'Funcionario não encontrado.'})
    return jsonify({'id': funcionario.id, 'nome': funcionario.nome, 'cargo': funcionario.cargo, 'salario': funcionario.salario})

@app.route('/funcionarios', methods=['POST'])
def add_funcionario():
    nome = request.json['nome']
    cargo = request.json['cargo']
    salario = request.json['salario']
    novo_funcionario = Funcionario(nome, cargo, salario)
    db.session.add(novo_funcionario)
    db.session.commit()
    return jsonify({'message': 'Novo funcionario adicionado com sucesso.'})

@app.route('/funcionarios/<id>', methods=['PUT'])
def update_funcionario(id):
    funcionario = Funcionario.query.filter_by(id=id).first()
    if not funcionario:
        return jsonify({'message': 'Funcionario não encontrado.'})
    nome = request.json['nome']
    cargo = request.json['cargo']
    salario = request.json['salario']
    funcionario.nome = nome
    funcionario.cargo = cargo
    funcionario.salario = salario
    db.session.commit()
    return jsonify({'message': 'Funcionario atualizado com sucesso.'})

@app.route('/funcionarios/<id>', methods=['DELETE'])
def delete_funcionario(id):
    funcionario = Funcionario.query.filter_by(id=id).first()
    if not funcionario:
        return jsonify({'message': 'Funcionario não encontrado.'})
    db.session.delete(funcionario)
    db.session.commit()
    return jsonify({'message': 'Funcionario deletado com sucesso.'})

if __name__ == '__main__':
    app.run(debug=True)
