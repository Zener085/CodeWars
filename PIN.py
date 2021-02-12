def validate_pin(pin):
    return True if (len(pin) == 4 or len(pin) == 6)\
                     and (set(pin).intersection(set('1234567890')) == set(pin)) else False