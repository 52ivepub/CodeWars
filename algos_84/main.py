


url = ''

hex_string = "#FF9933"
# ), {'r':255, 'g':153, 'b':51}


def hex_string_to_RGB(hex_string):
    hex_string = hex_string[1:]
    result = {"r": 0, "g": 0, "b": 0}
    for x, y in result.items():
        result[x] = int((hex_string[0:2]), 16)
        hex_string = hex_string[2:]
    return  result





print(hex_string_to_RGB(hex_string))