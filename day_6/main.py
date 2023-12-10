import math

with open('input') as f:
    my_input = f.readlines()

my_input = [line.rstrip().split(':')[1].strip() for line in my_input]
my_input = [one_input.split(' ') for one_input in my_input]
my_input = [[int(elem) for elem in one_input if elem != '']
            for one_input in my_input]
my_input = [(my_input[0][i], my_input[1][i]) for i in range(len(my_input[0]))]

acc = 1
for time, distance in my_input:
    if time ** 2 - 4 * distance < 0:
        acc = 0
    else:
        push_time_low = (time - math.sqrt(time ** 2 - 4 * distance)) / 2
        push_time_high = (time + math.sqrt(time ** 2 - 4 * distance)) / 2
        push_time_low = math.floor(push_time_low)
        push_time_high = math.ceil(push_time_high)
        acc *= math.floor(push_time_high) - math.ceil(push_time_low) - 1

print(acc)

