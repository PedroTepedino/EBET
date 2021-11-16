from datetime import datetime, date

def calculate_age(birth_date_string):
    birth_date_string = birth_date_string.replace('-', '/') + ''
    birth_date =  datetime.strptime(birth_date_string, '%Y/%m/%d').date()
    today = date.today()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
