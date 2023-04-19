#Gabriel de jesus alves
#Ra:1901453

from flask import Flask, jsonify, request

app = Flask(__name__)

cuecasbox = [
    {
        'id': 1,
        'Tamanho': 'P',
        'Cor': 'Vermelha'
    },
    {
        'id': 2,
        'Tamanho': 'M',
        'Cor': 'Amarela',
    },
    {
        'id': 3,
        'Tamanho': 'G',
        'Cor': 'Azul',
    },
    {
        'id': 4,
        'Tamanho': 'GG',
        'Cor': 'Verde'
    },
]

#consulta

@app.route('/cuecasbox', methods=['GET'])
def obter_cuecasbox():
    return jsonify(cuecasbox), 200


# consulta por id


@app.route('/cuecasbox/<int:id>', methods=['GET'])
def obter_cuecasbox_por_id(id):
    for cuecasbox in cuecasbox:
        if cuecasbox.get('id') == id:
            return jsonify(cuecasbox), 404


app.run(port=5001, host='localhost', debug=True)
