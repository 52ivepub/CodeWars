st = "The quick brown fox jumps over the lazy dog."
      # "Cwmalgos_10 fjord bank glyphs vext quiz",


def is_pangram(st):
    alphavit = [chr(i) for i in range(97, 123)]
    for i in st.lower():
        if i in alphavit:
            alphavit.remove(i)
    return len(alphavit) == 0

print(is_pangram(st))