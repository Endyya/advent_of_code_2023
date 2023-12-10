import itertools as itt

code = {}
with open('input') as f:
    loop = f.readline().rstrip()

    line = f.readline()
    line = f.readline().rstrip()

    while line != '':
        parsing = line.split('=')
        parsing[1] = parsing[1].replace(')', '')
        parsing[1] = parsing[1].replace('(', '')
        parsing[1] = parsing[1].replace(' ', '')
        code[parsing[0].strip()] = parsing[1].split(',')
        line = f.readline().rstrip()

position = 'AAA'

counter = 0
for instruction in itt.cycle(loop):
    if position == 'ZZZ':
        break
    else:
        counter += 1
        if instruction == 'L':
            position = code[position][0]
        else:
            position = code[position][1]

print('part 1 : ', counter)
    
