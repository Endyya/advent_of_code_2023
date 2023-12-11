import itertools as itt

code = {}
part_2_pos = []
with open('input') as f:
    loop = f.readline().rstrip()

    line = f.readline()
    line = f.readline().rstrip()

    while line != '':
        if parsing[0].rstrip()[-1] == 'A':
            part_2_pos.append(parsing[0].rstrip())
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
    
for instruction in itt.cycle(loop):
    if [elem[-1] for elem in part_2_pos] == ['Z'] * len(part_2_pos):
        break
    else:
        counter += 1
        for i, position in enumerate(part_2_pos):
            if instruction == 'L':
                position = code[position][0]
            else:
                position = code[position][1]
            part_2_pos[i] = position

print(counter)
