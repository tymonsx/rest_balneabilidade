from flask import Flask, escape, request, jsonify, json
from markupsafe import escape
import pandas as pandas
from flask_cors import CORS, cross_origin
from statsmodels.tsa.statespace.sarimax import SARIMAXResults
from datetime import date

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
    
##@app.route('/previsaoProximaSemana', methods=['GET'])
##def preveProximaSemana():
    ##loaded = SARIMAXResults.load('model.pkl')
    ##conversaoEmLista = loaded.get_forecast(steps=5).predicted_mean.to_numpy().tolist()
    ##response = app.response_class(
        ##response=json.dumps(conversaoEmLista),
        ##status=200,
        ##mimetype='application/json'
    ##)
    ##return response
    
@app.route('/previsaoProximasCincoSemanas', methods=['GET'])
def preveProximasCincoSemanas():
    loaded = SARIMAXResults.load('model.pkl')
    
    hoje = date.today()
    ultimaData = date(2020, 3, 15)
    medicoesInicio = (hoje-ultimaData).days/7
    numMedicoes=medicoesInicio+5
    primeiraData='2020-03-22'
    
    predicao=loaded.get_forecast(steps=34)
    predicao.predicted_mean
    
    index_date = pandas.date_range(primeiraData, periods = numMedicoes, freq = 'W')
    forecast_series = pandas.Series(list(predicao.predicted_mean), index = index_date)
    
    
    conversaoEmLista = pandas.DataFrame(data=forecast_series).tail(5).to_numpy().tolist()
    response = app.response_class(
        response=json.dumps(conversaoEmLista),
        status=200,
        mimetype='application/json'
    )
    return response