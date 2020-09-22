# rest_balneabilidade

Servidor Rest em python para servir os dados e funções de predição de balneabilidade das praias de são paulo

1 - Criação do ambiente:
conda create -n [nome_do_ambiente]
Instalar no novo ambiente o “PowerShell Prompt” e o “Jupyter Notebook”

2 - Instalação das principais bibliotecas/frameworks dentro do “PowerShell Prompt”:
PANDAS: conda install -c anaconda pandas
FLASK: conda install -c anaconda flask
FLASK-CORS: conda install -c anaconda flask-cors

3 - Rodar o webservice dentro do “PowerShell Prompt”:
\$env:FLASK_APP = "[nome_do_arquivo].py"
flask run
