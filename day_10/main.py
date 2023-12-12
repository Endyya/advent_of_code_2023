import numpy as np

class NoMoreUpdateException(Exception):
    pass

def next_indexes(symbol, i, j):
    if symbol == '|':
        return [(i - 1, j), (i + 1, j)]
    elif symbol == '-':
        return [(i, j - 1), (i, j + 1)]
    elif symbol == 'F':
        return [(i + 1, j), (i, j + 1)]
    elif symbol == 'J':
        return [(i - 1, j), (i, j - 1)]
    elif symbol == 'L':
        return [(i - 1, j), (i, j + 1)]
    elif symbol == '7':
        return [(i, j - 1), (i + 1, j)]
    elif symbol == 'S':
        return [(int(i + 1), int(j)),
                (int(i - 1), int(j)),
                (int(i), int(j + 1)),
                (int(i), int(j - 1))]
    elif symbol == '.':
        return []
    else:
        print(symbol)
        raise Exception

def get_missing_pos(data, i, j):
    neigh_pos = [(int(i + 1), int(j)),
                 (int(i - 1), int(j)),
                 (int(i), int(j + 1)),
                 (int(i), int(j - 1))]

    elements = {
        'up' : '.',
        'down' : '.',
        'left' : '.',
        'right' : '.'}
    for pos in neigh_pos:
        letter = data[pos]
        if pos == (i + 1, j) and i <= data.shape[0]:
            elements['down'] = letter
        elif pos == (i - 1, j) and i > 0:
            elements['up'] = letter
        elif pos == (i, j + 1) and j <= data.shape[1]:
            elements['right'] = letter
        elif pos == (i, j - 1) and j > 0:
            elements['left'] = letter

    if elements['up'] in '7|F' and elements['down'] in 'J|L':
        return '|'
    elif elements['up'] in '7|F' and elements['right'] in 'J-7':
        return 'L'
    elif elements['up'] in '7|F' and elements['left'] in 'L-F':
        return 'J'    
    elif elements['left'] in 'L-F' and elements['right'] in 'J-7':
        return '-'
    elif elements['left'] in 'L-F' and elements['down'] in 'J|L':
        return '7'    
    elif elements['down'] in 'J|L' and elements['right'] in 'J-7':
        return 'F'
    else:
        return '.'

        

def way_length_update(data, way_length, cur_pos):
    new_indexes = next_indexes(data[cur_pos], *cur_pos)

    for i, j in new_indexes.copy():
        if (i < 0 or j < 0
            or i >= data.shape[0] or j >= data.shape[1]
            or way_length[i, j] != -1):
            new_indexes.pop(new_indexes.index((i, j)))

    # if len(new_indexes) == 0:
    #     print(data, way_length, cur_pos)
    #     raise NoMoreUpdateException

    for i, j in new_indexes:
        way_length[i, j] = way_length[cur_pos] + 1


with open('input') as f:
    lines = f.readlines()

# remove \n 
lines = [line.rstrip() for line in lines]

# build data
data = np.array([char for line in lines for char in line], dtype = str)
data.shape = (len(data) // len(lines), len(lines))

# initialize way_length
way_length = np.full(data.shape, -1)
starting_pos = np.where(data == 'S')
way_length[starting_pos] = 0

i, j = starting_pos

new_pos = [(int(i + 1), int(j)),
           (int(i - 1), int(j)),
           (int(i), int(j + 1)),
           (int(i), int(j - 1))]

# Remove invalid positions and make 1st step
for i, j in new_pos.copy():
    if i < 0 or j < 0 or i >= data.shape[0] or j >= data.shape[1]:
        new_pos.pop(new_pos.index((i, j)))
    elif starting_pos in next_indexes(data[i, j], i, j):
        way_length[i, j] = 1
    else:
        new_pos.pop(new_pos.index((i, j)))

cur_pos = np.transpose(np.where(way_length == 1))

data[starting_pos] = get_missing_pos(data, *starting_pos)

counter = 1

while len(cur_pos) > 0:
    counter += 1
    next_positions = []
    for i, j in cur_pos:
        next_positions.append(next_indexes(data[i, j], i, j))
    next_positions = [position for positions in next_positions
                      for position in positions]
    for i, j in next_positions.copy():
        if i < 0 or j < 0 or i >= data.shape[0] or j >= data.shape[1]:
            next_positions.pop(next_positions.index((i, j)))
        elif way_length[i, j] != -1:
            next_positions.pop(next_positions.index((i, j)))
        else:
            way_length[i, j] = counter

    
    cur_pos = next_positions

print(np.max(way_length))
