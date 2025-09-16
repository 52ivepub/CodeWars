
url = ''


lines = ["a", "b", "c"]
# ), ["1: a", "2: b", "3: c"]

def number(lines):
   return [f'{num}: {char}' for num, char in enumerate(lines, start=1)]






print(number(lines))