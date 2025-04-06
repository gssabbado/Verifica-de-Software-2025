from negative_power_error import NegativeError

def power_to(b, e):
    if e < 0: 
        raise NegativeError()
    return b **e
