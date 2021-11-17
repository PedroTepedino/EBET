from datetime import datetime, date
from hashlib import md5

def calculate_age(birth_date_string):
    birth_date_string = birth_date_string.replace('-', '/') + ''
    birth_date =  datetime.strptime(birth_date_string, '%Y/%m/%d').date()
    today = date.today()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

def hash_password(password):
    return md5(password.encode('utf-8')).hexdigest()

