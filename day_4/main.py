









with open('input') as f:
    line = f.readline().rstrip()
    score_1 = 0

    while line != '':
        head, tail = line.split(':')
        win, our = tail.split('|')
        set_win = set(win.split())
        set_our = set(our.split())
        good_numbers = set_our.intersection(set_win)
        if len(good_numbers) > 0:
            score_1 += 2 ** (len(good_numbers) - 1)
        line = f.readline().rstrip()


print('part 1 : ', score_1)
