import mysql.connector
import locale
import bd
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/cadastrar')
def cadastro():
    return render_template('cadastrar.html')


@app.route('/cadastro', methods=['POST'])
def cadastro2():
    is_valid_request = True #admits valid input
    msg = ''

    nome = request.form['nome']
    if not nome.replace(' ', '').isalpha():
        is_valid_request = False
        msg += 'O nome deve conter apenas letras\n'

    data = request.form['data']
    cpf = request.form['cpf']
    email = request.form['email']
    username = request.form['username']
    
    senha = request.form['senha']
    confsenha = request.form['confsenha']
    if senha != confsenha:
        is_valid_request = False
        msg += "As senhas nao são iguais\n"

    if is_valid_request:
        mysql = bd.SQL("root", "hiragi7", "ebet")
        comando = "INSERT INTO apostador(nmecomp_ap, datanasc_ap, cpf_ap, email_ap, username_ap, senha_ap, confsenha_ap) VALUES (%s, %s, %s, %s, %s, %s, %s);"
        if mysql.executar(comando, [nome, data, cpf, email, username, senha, confsenha]):
            msg = "Cadastro realizado com sucesso!"
        else:
            msg = "Falha no cadastro. Tente novamente!"

    return render_template('cadastro.html', msg=msg)




app.debug = 1
app.run()
