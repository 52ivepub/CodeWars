url = ''

morse_code = '.... . -.--   .--- ..- -.. .'


# from preloaded import MORSE_CODE

def decode_morse(morse_code):
    # Remember - you can use the preloaded MORSE_CODE dictionary:
    # For example:
    # MORSE_CODE['.-'] = 'A'
    # MORSE_CODE['--...'] = '7'
    # MORSE_CODE['...-..-'] = '$'
    out = ''
    for i in morse_code.split('   '):
        for x in i.split():
            out += MORSE_CODE[x]
        out += ' '
    return out.strip()



print(decode_morse(morse_code))

x = [1, 2, 3]
print(x[:-1])





