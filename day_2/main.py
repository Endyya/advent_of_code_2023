def parse_grab(grab):
    grab_content = grab.split(',')
    green = blue = red = 0
    content = {'green' : green,
               'blue' : blue,
               'red' : red}

    for one_grab in grab_content:
        number = int(one_grab.split(' ')[1])
        color = one_grab.split(' ')[2]
        content[color] = number
    return content
        
    

def parse(line, part = 1):
    header, content = line.split(':')
    game_ID = int(header.split('Game')[-1])
    bags = content.split(';')
    max_green = max_blue = max_red = 0
    for bag in bags:
        content = parse_grab(bag)
        max_green = max(max_green, content['green'])
        max_red = max(max_red, content['red'])
        max_blue = max(max_blue, content['blue'])        
    inside = line.split(':')[1]

    return game_ID, max_red, max_green, max_blue



with open("input") as f:
    line = f.readline()
    result = 0

    while line != '':
        game_ID, max_red, max_green, max_blue = parse(line)

        if (max_blue <= 14 and max_red <= 12 and max_green <= 13):
            result += game_ID




        line = f.readline()

    print(result)
