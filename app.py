from datetime import timedelta

from flask import (
    Flask,
    render_template,
    request,
    session,
    url_for,
    redirect
)

from utils import *
from validations import *

app = Flask(__name__)
app.secret_key = 'somesecretkeythatonlyishouldknow'


@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)


@app.route('/')
def login():
    if session.get('user_id'):
        return redirect(url_for('menu'))

    return render_template('login.html')


@app.route('/cadastrar')
def cadastro():
    return render_template('cadastrar.html')


@app.route('/cadastro', methods=['POST'])
def cadastro2():
    mysql = bd.SQL("ENhmDU84Vz", "kdEBNUvuo4", "ENhmDU84Vz", "remotemysql.com", "3306")

    is_valid_request = True  # admits valid input
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
    if result is not None:
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
        comando = "INSERT INTO apostador(nmecomp_ap, datanasc_ap, cpf_ap, email_ap, username_ap, senha_ap) VALUES (%s, %s, %s, %s, %s, SHA(%s));"
        if mysql.executar(comando, [nome, data, cpf, email, username, senha]):
            msg = "Cadastro realizado com sucesso!"
        else:
            msg = "Falha no cadastro. Tente novamente!"

    return render_template('cadastro.html', msg=msg)


@app.route('/menu', methods=['GET', 'POST'])
def menu():
    if session.get('user_id') and session['user_id'] != 0:
        return render_template('menu.html')

    username = request.form['username']
    senha = request.form['senha']

    mysql = bd.SQL("ENhmDU84Vz", "kdEBNUvuo4", "ENhmDU84Vz", "remotemysql.com", "3306")
    cmd = 'SELECT idt_ap AS id FROM apostador WHERE username_ap=%s AND senha_ap=SHA(%s);'

    id = mysql.consultar(cmd, [username, senha]).fetchone()
    if id[0] != 0:
        session['user_id'] = id[0]
        session['username'] = username
        return render_template('menu.html')
    else:
        return render_template('err.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/go-to-tests')
def render_tests():
    return render_template('test.html')


@app.route('/test', methods=['POST'])
def test():
    return render_template('test.html')


@app.route('/adicionar_jogo')
def adicionar():
    if not session.get('user_id'):
        return redirect(url_for('login'))

    return render_template('adicionar_jg.html')


@app.route('/adicionado_jogo', methods=['POST'])
def adicionar2():
    if not session.get('user_id'):
        return redirect(url_for('login'))

    jogo = request.form['jogo']
    modalidade = request.form['modalidade']
    descricao = request.form['descricao']

    mysql = bd.SQL("ENhmDU84Vz", "kdEBNUvuo4", "ENhmDU84Vz", "remotemysql.com", "3306")
    comando = "INSERT INTO jogo(nme_jg, modalidade_jg, desc_jg) VALUES (%s, %s, %s);"
    if mysql.executar(comando, [jogo, modalidade, descricao]):
        msg = jogo + " adicionado com sucesso!"
    else:
        msg = "Falha na inclusão de jogo."
    return render_template('adicionado_jg.html', msg=msg)


@app.route('/adicionar_time')
def adicionar3():
    if not session.get('user_id'):
        return redirect(url_for('login'))
    return render_template('adicionar_tm.html')


@app.route('/adicionado_time', methods=['POST'])
def adicionar4():
    if not session.get('user_id'):
        return redirect(url_for('login'))

    time = request.form['time']
    sigla = request.form['sigla']
    num_players = float(request.form['num_players'])

    mysql = bd.SQL("ENhmDU84Vz", "kdEBNUvuo4", "ENhmDU84Vz", "remotemysql.com", "3306")
    comando = "INSERT INTO time(nme_tm, sgl_tm, num_plys_tm) VALUES (%s, %s, %s);"
    if mysql.executar(comando, [time, sigla, num_players]):
        msg = time + " adicionado com sucesso!"
    else:
        msg = "Falha na inclusão de time."

    return render_template('adicionado_tm.html', msg=msg)


@app.route('/adicionar_partida')
def adicionar5():
    if not session.get('user_id'):
        return redirect(url_for('login'))

    return render_template('adicionar_pt.html')


@app.route('/adicionado_partida', methods=['POST'])
def adicionar6():
    if not session.get('user_id'):
        return redirect(url_for('login'))

    odds_a = request.form['odds_a']
    odds_b = request.form['odds_b']
    results = request.form['results']
    rounds = request.form['rounds']
    values_a = request.form['values_a']
    values_b = request.form['values_b']
    idt1_time = request.form['idt1_time']
    idt2_time = request.form['idt2_time']
    idt_jogo = request.form['idt_jogo']

    mysql = bd.SQL("ENhmDU84Vz", "kdEBNUvuo4", "ENhmDU84Vz", "remotemysql.com", "3306")

    comando = "INSERT INTO partida(odds_a_pt, odds_b_pt, results_pt, rounds_pt, values_a_pt, values_b_pt, idt1_time, idt2_time, idt_jogo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
    if mysql.executar(comando, [odds_a, odds_b, results, rounds, values_a, values_b, idt1_time, idt2_time, idt_jogo]):
        msg = "Partida adicionada com sucesso!"
    else:
        msg = "Falha na inclusão de partida."

    return render_template('adicionar_pt.html', msg=msg)


@app.route('/apostas')
def apostas():
    if not session.get('user_id'):
        return redirect(url_for('login'))

    return render_template('apostas.html')


@app.route('/carteira')
def carteira():
    if not session.get('user_id'):
        return redirect(url_for('login'))

    return render_template('carteira.html')


@app.route('/conta')
def conta():
    if not session.get('user_id'):
        return redirect(url_for('login'))

    return render_template('conta.html')


app.debug = 1
app.run()
