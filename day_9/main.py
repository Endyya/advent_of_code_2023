import numpy as np

def get_next_value(number_list):
    cur_number = number_list
    while cur_number:
        pass


part_1_value = 0
part_2_value = 0

data = np.loadtxt('input', dtype = np.int32)
data = data[:, :, np.newaxis]
cur_data = data

count = 0
while not np.array_equal(data[:, :, -1],
                         np.zeros(shape = data[:, :, -1].shape,
                                  dtype = np.int32)):
    new_data_shape = [*data.shape]
    new_data_shape[-1] += 1
    new_layer = np.zeros(shape = tuple(new_data_shape), dtype = np.int32)
    new_layer[:, :, :-1] = data
    new_layer[:, (count + 1):, -1] = (data[:, count+1:, -1]
                                      - data[:, count:-1, -1])

    data = new_layer
    
    count += 1

print('part 1 : ', np.sum(data[:, -1, :]))

data = np.diagonal(data, axis1 = 1, axis2 = 2)

mask = np.zeros(data.shape, dtype = np.int32)

new_data = np.zeros(data.shape, dtype = np.int32)

for i in range(data.shape[0]):
    line = data[i, :]
    while line[-1] == 0:
        line = line[:-1]
    new_data[i, (len(data[i, :]) - len(line)):] = line

one_line_mask = [(-1) ** i for i in range(new_data.shape[1])]

mask = np.array(one_line_mask * data.shape[0]).reshape(new_data.shape)

print('part 2 : ', np.sum(mask * data))



