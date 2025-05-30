import re

def validate(email):
    if not email or not isinstance(email, str):
        return False

    if len(email) > 320: # Mutante 1 - If_statement to if_false
        return False     # Mutante 2 - Return None

    if '@' not in email or email.count('@') != 1: # Mutante 3 - not equal to Gt (">")
        return False

    local_part, domain = email.split('@')

    if not local_part or not domain: # Mutante 4 - Or to And
        return False

    if len(local_part) > 64 or len(domain) > 255:
        return False

    # Local part rules
    if '..' in local_part or local_part.endswith('.') or ' ' in local_part:
        return False

    # Domain part rules
    domain_labels = domain.split('.')
    if any(len(label) > 63 for label in domain_labels):
        return False # Mutante 5 - False to None

    # Use a safe regex to confirm valid characters and structure
    local_pattern = r'^[A-Za-z0-9!#$%&\'*+/=?^_`{|}~.-]+$'
    domain_pattern = r'^[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

    if not re.match(local_pattern, local_part):
        return False

    if not re.match(domain_pattern, domain):
        return False

    return True