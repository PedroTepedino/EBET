import re
from datetime import datetime, date
from hashlib import md5

import bd


def calculate_age(birth_date_string):
    birth_date_string = birth_date_string.replace('-', '/') + ''
    birth_date =  datetime.strptime(birth_date_string, '%Y/%m/%d').date()
    today = date.today()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

def hash_password(password):
    return md5(password.encode('utf-8')).hexdigest()

def normalize_cpf(cpf_string):
    cpf_string = cpf_string.replace('.', '').replace('-', '')
    separated_cpf = re.findall('...?', cpf_string)
    cpf_string = separated_cpf[0] + "." + separated_cpf[1] + '.' + separated_cpf[2] + '-' + separated_cpf[3]
    return cpf_string

if __name__ == "__main__":
    mysql = bd.SQL("ENhmDU84Vz", "kdEBNUvuo4", "ENhmDU84Vz", "remotemysql.com", "3306")
    print(normalize_cpf("12345678910"))
    comando = "SELECT idt_ap FROM apostador WHERE cpf_ap = %s"
    print(mysql.consultar(comando, ["12346578910"]).fetchone())
