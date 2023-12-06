

class Engine():

    def __init__(self):
        self.engine_part = []

    def __repr__(self):
        rep = ''
        
        for part in self.engine_part:
            rep += part.__repr__() + '\n'

        return rep

    def add_part(self, engine_part):
        self.engine_part.append(engine_part)

    def get_neighbours(self, part):
        neighbours = []
        for inpart in self.engine_part:
            diff_x = abs(part.x - inpart.x)
            diff_y_prev = part.start_y - inpart.end_y
            diff_y_post = part.end_y - inpart.start_y
            is_same = (diff_x == 0 and part.start_y == inpart.start_y
                       and part.end_y == inpart.end_y)
            if (diff_x <= 1 and (diff_y_prev - 1) * (diff_y_post + 1) <= 0
                and not is_same):
                neighbours.append(inpart)

        return neighbours
                
            
class EnginePart():

    def __init__(self, x, start_y, end_y):
        self.x = x
        self.start_y = start_y
        self.end_y = end_y

    def __repr__(self):
        rep = ''

        rep += f'x = {self.x}\n'
        rep += f'y from {self.start_y} to {self.end_y}'

        return rep
    
class Number(EnginePart):

    def __init__(self, number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.number = number

    def __repr__(self, *args, **kwargs):
        return f'Number : {self.number} \n' + super().__repr__(*args, **kwargs)

class Symbol(EnginePart):

    def __init__(self, symbol, *args, **kwargs):
        super().__init__(*args, **kwargs)        
        self.symbol = symbol

    def __repr__(self, *args, **kwargs):
        return f'Symbol : {self.symbol} \n' + super().__repr__(*args, **kwargs)


def parse(engine, line, line_num):
    acc = 0
    start = -1
    for col, cell in enumerate(list(line)):
        if cell in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if start == -1:
                start = col
            acc = 10 * acc + int(cell)
        else:
            if acc != 0:
                new_number = Number(number = acc, x = line_num,
                                    start_y = start, end_y = col - 1)
                engine.add_part(new_number)
                acc = 0
                start = -1
            if  cell != '.':
                new_symbol = Symbol(symbol = cell, x = line_num,
                                    start_y = col, end_y = col)
                engine.add_part(new_symbol)
    if acc != 0:
        new_number = Number(number = acc, x = line_num,
                            start_y = start, end_y = col - 1)
        engine.add_part(new_number)        

                
with open('input') as f:
    line = f.readline().rstrip()
    my_engine = Engine()
    line_num = 0
    while line != '':
        parse(my_engine, line, line_num)
        line_num += 1

        line = f.readline().rstrip()

    score = 0
        
    for part in my_engine.engine_part:
        if isinstance(part, Number):

            test = False
            for neighbour in my_engine.get_neighbours(part):
                test = test or isinstance(neighbour, Symbol)
            if test:
                score += part.number
                    

    print('part 1 sum : ', score)

