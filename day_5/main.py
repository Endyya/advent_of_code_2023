import numpy as np

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

    number = seeds_line
    
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

        # initialize the map
        my_map = list(range(max_val + 1))

        # create the map

        for code in table:
            my_map[code[1]:(code[1] + code[2])] = range(code[0],
                                                        code[0] + code[2])

        number = [my_map[i] for i in number]

    print(min(*number))
        

        

        



