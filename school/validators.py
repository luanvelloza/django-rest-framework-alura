import re
from validate_docbr import CPF

def is_name_valid(name):
        return not name.isalpha()

def is_cpf_valid(cpf_number):
        cpf = CPF()
        return not cpf.validate(cpf_number)

def is_phone_number_valid(phone_number):
        pattern = '[0-9]{2} [0-9]{5}-[0-9]{4}'
        validation = re.findall(pattern, phone_number)
        return not validation 