import math
import itertools as itt

code = {}
part_2_pos = []
with open('input') as f:
    loop = f.readline().rstrip()

    line = f.readline()
    line = f.readline().rstrip()

    while line != '':
        parsing = line.split('=')
        if parsing[0].rstrip()[-1] == 'A':
            part_2_pos.append(parsing[0].rstrip())

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

# Dataset is organized in 6 disjoint cycles, one cycle can only ends
# simultaneously with the end of the input direction (4 repetition of R)


def align_cycles(starts, ends):
    return_start = starts
    return_end = []
    for start in starts:
        cur_pos = start
        while not cur_pos in ends:
            cur_pos = code[cur_pos][1]
        return_end.append(cur_pos)
    return return_start, return_end

start = [pos for pos in code.keys() if pos[-1] == 'A']
end = [pos for pos in code.keys() if pos[-1] == 'Z']

start, end = align_cycles(start, end)

def order(pos, code, input_line):
    ''' Compute the number of step to do one cycle, starting from pos'''

    return route_length(pos, pos, code, input_line)

def route_length(start_pos, end_pos, code, input_line):
    ''' Compute the number of step to go from start_pos to end_pos (possibly
    endless '''

    decode_instruction = {'L': 0, 'R': 1}
    cur_pos = start_pos
    loop = input_line
    first_loop = True
    counter = 0
    for instruction in itt.cycle(loop):
        cur_pos = code[cur_pos][decode_instruction[instruction]]
        counter += 1
        if cur_pos == end_pos:
            break

    return counter

# Get the order of each end
orders = [order(e, code, loop) for e in end]

# Get the time to go from each start to one end
mods = [route_length(spos, epos, code, loop) for spos, epos in zip(start, end)]

# In this dataset, the time to get first to each end is the same to the order
# of each end
assert orders == mods


for i, j in itt.product(range(len(mods)), range(len(mods))):
    if i != j:
        gcd = math.gcd(mods[i], mods[j])
        first_remainder = route_length(start[i], end[i], code, loop)
        second_remainder = route_length(start[j], end[j], code, loop)
        
        # Check chinese remainders generalized hypotheses
        assert ((first_remainder - second_remainder) % gcd == 0)

        # In this dataset, each remainder is divided by gcd
        assert first_remainder % gcd == 0
        assert second_remainder % gcd == 0        

# The problem solution is then the lowest common mmultiple of all ends orders
lcm = 1
for mod in mods:
    lcm = math.lcm(lcm, mod)

print('part 2 : ', lcm)
        
    








        
