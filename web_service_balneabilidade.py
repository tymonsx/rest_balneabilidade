from flask import Flask, escape, request, jsonify, json
from markupsafe import escape
import pandas as pandas
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def hello():
    return 'Bem vindo!'
    
@app.route('/todosResultados', methods=['GET'])
def retornaTodosResultados():
    cidade = request.args.get('cidade')
    print(cidade)
    praia = request.args.get('praia')
    print(praia)
    dataFrameCsv = pandas.read_csv('sp_beaches_update.csv')
    print(dataFrameCsv[(dataFrameCsv["City"] == cidade.upper()) & (dataFrameCsv["Beach"] == praia.upper())])
    dataFrameCsv = dataFrameCsv[(dataFrameCsv["City"] == cidade.upper()) & (dataFrameCsv["Beach"] == praia.upper())]
    conversaoEmLista = dataFrameCsv[['Date','Enterococcus']].to_numpy().tolist()
    response = app.response_class(
        response=json.dumps(conversaoEmLista),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/resultadosUltimosDoisAnos', methods=['GET'])
def resultadosUltimosDoisAnos():
    cidade = request.args.get('cidade')
    praia = request.args.get('praia')
    dataFrameCsv = pandas.read_csv('sp_beaches_update.csv')
    print(dataFrameCsv[(dataFrameCsv["City"] == cidade.upper()) & (dataFrameCsv["Beach"] == praia.upper())])
    dataFrameCsv = dataFrameCsv[(dataFrameCsv["City"] == cidade.upper()) & (dataFrameCsv["Beach"] == praia.upper())].tail(104)
    conversaoEmLista = dataFrameCsv[['Date','Enterococcus']].to_numpy().tolist()
    response = app.response_class(
        response=json.dumps(conversaoEmLista),
        status=200,
        mimetype='application/json'
    )
    return response
    
##@app.route('/ultimasCincoSemanas', methods=['GET'])
##def retornaUltimasCincoSemanas():
    ##cidade = request.args.get('cidade')
    ##print(cidade)
    ##praia = request.args.get('praia')
    ##print(praia)
    ##dataFrameCsv = pandas.read_csv('sp_beaches_update.csv')
    ##print(dataFrameCsv[(dataFrameCsv["City"] == cidade.upper()) & (dataFrameCsv["Beach"] == praia.upper())].tail(5))
    ##conversaoEmListaDois = dataFrameCsv[(dataFrameCsv["City"] == cidade.upper()) & (dataFrameCsv["Beach"] == praia.upper())].tail(5).to_numpy().tolist()
    ##response = app.response_class(
        ##response=json.dumps(conversaoEmListaDois),
        ##status=200,
        ##mimetype='application/json'
    ##)
    ##return response
    
@app.route('/proximaSemana', methods=['GET'])
def preveProximaSemana():
    cidade = request.args.get('cidade')
    print(cidade)
    praia = request.args.get('praia')
    print(praia)
    data = request.args.get('data')
    print(data)
    return 'PRÓXIMA SEMANA - Cidade: {}, Praia: {}, Data: {}'.format(cidade,praia, data)
    
@app.route('/proximasCincoSemanas', methods=['GET'])
def preveProximasCincoSemanas():
    cidade = request.args.get('cidade')
    print(cidade)
    praia = request.args.get('praia')
    print(praia)
    data = request.args.get('data')
    print(data)
    return 'PRÓXIMAS 5 SEMANAS - Cidade: {}, Praia: {}, Data: {}'.format(cidade,praia, data)