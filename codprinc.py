import mysql.connector
import locale
import bd
from flask import Flask, render_template, request
from datetime import date
from utils import *
from validations import *

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
    if (calculate_age(data) < 18):
        is_valid_request = False
        msg += "Idade invalida. E necessario ter mais de 18 anos!\n"

    cpf = request.form['cpf']
    if not validate_cpf(cpf):
        is_valid_request = False
        msg += "CPF Invalido\n"

    email = request.form['email']
    if not validate_email(email):
        is_valid_request = False
        msg += "Email invalido\n"
    
    username = request.form['username']
    if not validate_username(username):
        is_valid_request = False
        msg += "Username shoud only contain letters, numbers.\n"
    
    senha = request.form['senha']
    confsenha = request.form['confsenha']
    if senha != confsenha:
        is_valid_request = False
        msg += "As senhas nao são iguais\n"

    if is_valid_request:
        mysql = bd.SQL("ebet", "ebet", "ebetdb")
        comando = "INSERT INTO apostador(nmecomp_ap, datanasc_ap, cpf_ap, email_ap, username_ap, senha_ap, confsenha_ap) VALUES (%s, %s, %s, %s, %s, %s, %s);"
        if mysql.executar(comando, [nome, data, cpf, email, username, hash_password(senha), confsenha]):
            msg = "Cadastro realizado com sucesso!"
        else:
            msg = "Falha no cadastro. Tente novamente!"

    return render_template('cadastro.html', msg=msg)

@app.route('/go-to-tests')
def render_tests():
    return render_template('test.html')

@app.route('/test', methods=['POST'])
def test():
    password = request.form['senha']
    print(password)
    print(hash_password(password))
    return render_template('test.html')


app.debug = 1
app.run()
