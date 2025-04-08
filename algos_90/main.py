url = ''

pin = '-12345'

def validate_pin(pin):
    if not all([True if i.isnumeric() else False for i in pin]):
        return False
    if len(pin) == 4 or len(pin) == 6:
        return  True
    return False





print(validate_pin(pin))


