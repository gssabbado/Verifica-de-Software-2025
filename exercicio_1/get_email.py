import re
from invalid_syntax_error import InvalidSyntaxError

def my_email(email):
    pattern = "^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})$"
    match = re.fullmatch(pattern, email, 0)
    if match:
        print("Válido")
        return True
    else: raise InvalidSyntaxError()    
    
