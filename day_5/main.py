import numpy as np
import multiprocessing as mp

def my_input(seed_line, part = 2):
    if part == 2:
        for i in range(len(seed_line) // 2):
            start, my_range = seed_line[2 * i], seed_line[2 * i + 1]
            for j in range(start, start + my_range):
                yield j


def my_map(table, seed):
    for code in table:
        if seed >= code[1] and seed < code[1] + code[2]:
            return code[0] + seed - code[1]
    return seed

with open('input') as f:
    input_file = f.readlines()

    # clean empty lines
    input_file = [line for line in input_file if line != '\n']

# Parse seeds :
seeds_line = input_file[0].rstrip().split(':')[1].strip().split(' ')
seeds_line = [int(i) for i in seeds_line]

# Parse maps
headers = ['seed-to-soil map:\n',
           'soil-to-fertilizer map:\n',
           'fertilizer-to-water map:\n',
           'water-to-light map:\n',
           'light-to-temperature map:\n',
           'temperature-to-humidity map:\n',
           'humidity-to-location map:\n']

data = {}
next_header = -1

maps = {}
max_val = 0

number_1 = seeds_line
number_2 = seeds_line

for head in headers[::-1]:
    # get range indexes
    data_start = input_file.index(head)
    if next_header == -1:
        data_end = None
    else:
        data_end = input_file.index(next_header)
    next_header = head
    
    # Build the data dict
    data[head] = np.array([[int(i) for i in l.rstrip().split(' ')]
                           for l in input_file[(data_start + 1):data_end]])
    
    max_val = max(max_val, max(data[head][:, 1] + data[head][:, 2] - 1))

for head in headers:
    # load my data
    table = data[head]
    
    # get the new step location
    number_1 = [my_map(table, seed) for seed in number_1]

print('part 1 : ', min(*number_1))
    
number_2 = max_val

def one_seed(headers, data, seed):
    cur_number_2 = seed
    for head in headers:
        table = data[head]
        cur_number_2 = my_map(table, cur_number_2)
    return cur_number_2

with mp.Pool(16) as p:

    my_gen = my_input(seeds_line)
    my_counter = my_input(seeds_line)

    #del chunk
    
    while True:
        try:
            chunk = [next(my_gen, None) for _ in range(50000000)]
            chunk = [seed for seed in chunk if seed is not None]
            if len(chunk) == 0:
                break
            numbers_2 = p.map(lamb, chunk)
            number_2 = min(number_2, min(*numbers_2))
        except StopIteration:
            pass
            
print('part 2 : ', number_2)


        

        

        



