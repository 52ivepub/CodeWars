
url = ''

program = '''\
mov a 5
inc a
dec a
dec a
jnz a -1
inc a'''

def simple_assembler(program):
    seed = int(program.split()[2])
    # res = {program.split()[1]: 0}
    for i in program.split()[3:]:
        if i == 'inc':
            seed += 1
        elif i == 'dec':
            seed -= 1
        elif i == 'jnz':
            seed = 0

    return {program.split()[1]: seed}
print(simple_assembler(program))


