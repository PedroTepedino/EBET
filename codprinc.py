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
    mysql = bd.SQL("ENhmDU84Vz", "kdEBNUvuo4", "ENhmDU84Vz", "remotemysql.com", "3306")

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
    cpf = normalize_cpf(cpf)
    comando = "SELECT idt_ap FROM apostador WHERE cpf_ap = %s"
    cursor = mysql.consultar(comando, [cpf])
    result = cursor.fetchone()
    if len(result) > 0:
        is_valid_request = False
        msg += "CPF ja existe\n"


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
        comando = "INSERT INTO apostador(nmecomp_ap, datanasc_ap, cpf_ap, email_ap, username_ap, senha_ap) VALUES (%s, %s, %s, %s, %s, %s);"
        if mysql.executar(comando, [nome, data, cpf, email, username, hash_password(senha)]):
            msg = "Cadastro realizado com sucesso!"
        else:
            msg = "Falha no cadastro. Tente novamente!"

    return render_template('cadastro.html', msg=msg)

@app.route('/go-to-tests')
def render_tests():
    return render_template('test.html')

@app.route('/test', methods=['POST'])
def test():
    password = request.form['senha'].encode('utf-8')
    print(password)
    print(hash_password(password)).encode('utf-8')
    return render_template('test.html')

@app.route('/adicionar_jogo')
def adicionar():
    return render_template('adicionar_jg.html')

@app.route('/adicionado_jogo', methods=['POST'])
def adicionar2():
    jogo = request.form['jogo']
    modalidade = request.form['modalidade']
    descricao = request.form['descricao']

    mysql = bd.SQL("ENhmDU84Vz", "kdEBNUvuo4", "ENhmDU84Vz", "remotemysql.com", "3306")
    comando = "INSERT INTO jogo(nme_jg, modalidade_jg, desc_jg) VALUES (%s, %s, %s);"
    if mysql.executar(comando, [jogo, modalidade, descricao]):
       msg="Jogo" + jogo + " adicionado com sucesso!"
    else:
       msg="Falha na inclusão de jogo."
    return render_template('adicionar_jg.html')

@app.route('/adicionar_time')
def adicionar3():
    return render_template('adicionar_tm.html')

@app.route('/adicionado_time', methods=['POST'])
def adicionar4():
    time = request.form['time']
    sigla = request.form['sigla']
    num_players = float(request.form['num_players'])

    mysql = bd.SQL("ENhmDU84Vz", "kdEBNUvuo4", "ENhmDU84Vz", "remotemysql.com", "3306")
    comando = "INSERT INTO jogo(nme_tm, sgl_tm, num_plys_tm) VALUES (%s, %s, %s);"
    if mysql.executar(comando, [time, sigla, num_players]):
       msg="Time" + time + " adicionado com sucesso!"
    else:
       msg="Falha na inclusão de time."

    return render_template('adicionado_tm.html')

app.debug = 1
app.run()
