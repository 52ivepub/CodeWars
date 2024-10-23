sequence = 'AAAABBBCCDAABBB'
# ) == ['A', 'B', 'C', 'D', 'A', 'B']


def unique_in_order(sequence):
    res = [sequence[i] for i in range(0, len(sequence) - 1) if sequence[i] != sequence[i + 1]]
    if len(sequence) == 0:
        return res
    else:
        res.append(sequence[-1])
    return res



print(unique_in_order(sequence))