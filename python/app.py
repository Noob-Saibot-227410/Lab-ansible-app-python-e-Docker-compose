from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db/nomes.db'
db = SQLAlchemy(app)

class Nome(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    idade = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Nome {self.nome}, {self.idade}>"

@app.route('/nomes', methods=['POST'])
def criar_nome():
    nome = request.form.get('nome')
    idade = request.form.get('idade')
    novo_nome = Nome(nome=nome, idade=idade)
    db.session.add(novo_nome)
    db.session.commit()
    return jsonify({'id': novo_nome.id, 'nome': novo_nome.nome, 'idade': novo_nome.idade})

@app.route('/nomes', methods=['GET'])
def listar_nomes():
    nomes = Nome.query.all()
    return jsonify([{'id': n.id, 'nome': n.nome, 'idade': n.idade} for n in nomes])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
