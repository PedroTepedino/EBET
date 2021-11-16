import re

def validate_cpf(cpf_string):
    is_valid = re.search("^\d{3}\.?\d{3}\.?\d{3}-?\d{2}", cpf_string)
    if is_valid:
        return True
    else:
        return False

def validate_email(email_string):
    is_valid = re.search("^\w+@[a-z]+\.[a-z]+$", email_string)
    if is_valid:
        return True
    else:
        return False

def validate_username(username_string):
    if len(username_string) < 4:
        return False
    
    username_string = username_string.lower()
    is_valid = re.search("^[a-z]\w*$", username_string)
    if is_valid:
        return True
    else:
        return False
