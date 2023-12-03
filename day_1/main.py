



def parse(line, part = 1):
    base_trans = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if part == 2:
        translate = {'one' : '1',
                     'two' : '2',
                     'three' : '3',
                     'four' : '4',
                     'five' : '5',
                     'six' : '6',
                     'seven' : '7',
                     'eight' : '8',
                     'nine' : '9',
                     'zero' : '0'}
        translate = translate | dict(zip(base_trans, base_trans))

        for word in translate.keys():
            index = line.find(word)
            while index != -1:
                line = line[:index+1] + translate[word] + line[index:]
                print(index)
                print(line)
                index = line.find(word, index + 3)
            
        
    line = [i for i in line if i in base_trans]

    return int(''.join([line[0], line[-1]]))


# open the input file
with open("input") as f:
    calib_sum_1 = 0
    calib_sum_2 = 0

    line = f.readline()
    while line != "":
        calib_sum_1 += parse(line)
        calib_sum_2 += parse(line, part = 2)
        line = f.readline()

print("part 1 answer : ",calib_sum_1)
print("part 2 answer : ",calib_sum_2)


