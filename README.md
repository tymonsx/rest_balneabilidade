# rest_balneabilidade

Servidor Rest em python para servir os dados e funções de predição de balneabilidade das praias de São Paulo

## 1 - Criação do ambiente

```bash
conda create -n [nome_do_ambiente]
```

Instalar no novo ambiente o "PowerShell Prompt" e o “Jupyter Notebook” pelo Anaconda

## 2 - Instalação das principais bibliotecas/frameworks:

Realizar as instalações dentro do PowerShellPrompt

### Instalação do Pandas:

```
conda install -c anaconda pandas
```

### Instalação do Flask:

```
conda install -c anaconda flask
```

### Instalação do Flask-Cors:

```
conda install -c anaconda flask-cors
```

## 3 - Executar o webservice:

### Dentro do PowerShell Prompt:

```
$env:FLASK_APP = "[nome_do_arquivo].py"
flask run
```
