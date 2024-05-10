from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', resultado=(''))

@app.route('/planos')
def planos():
    return render_template('planos.html')

@app.route('/calculadora')
def calculadora():
    return render_template('tela-calculadora.html')

@app.route('/aulas')
def programas():
    return render_template('programas.html')

@app.route('/verificar', methods=['POST'])  # Define uma rota '/verificar' que aceita apenas requisições POST
def verificar():

    # Obtém o número enviado no formulário HTML e verifica o maior e o menor

    peso = float(request.form['peso'])
    altura = float(request.form['altura'])
    resultado = ""

    imc = peso / (altura * altura)

    if (imc <= 18.5):
        resultado="Abaixo do peso"
    elif ((imc > 18.5) and (imc <= 25)):
        resultado="Peso Normal"
    elif ((imc > 25) and (imc <= 30)):
        resultado="Sobrepeso"
    elif ((imc > 30) and (imc <= 35)):
        resultado="Obesidade grau 1"
    elif ((imc > 35) and (imc <= 40)):
        resultado="Obesidade grau 2"
    else:
        resultado="Obesidade grau 3"
    return render_template('tela-calculadora.html', resultado = resultado)

if __name__ == '__main__':
    # Inicia o servidor Flask em modo de depuração se este script for executado diretamente
    app.run(debug=True)
