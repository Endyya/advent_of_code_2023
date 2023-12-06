with open('input') as f:
    line = f.readline().rstrip()
    score_1 = 0
    deck = []

    while line != '':
        head, tail = line.split(':')
        card_number = int(head.split()[-1])
        deck.append(card_number)
        win, our = tail.split('|')
        set_win = set(win.split())
        set_our = set(our.split())
        good_numbers = set_our.intersection(set_win)
        if len(good_numbers) > 0:
            for _ in range(deck.count(card_number)):
                deck += list(range(card_number + 1,
                                   card_number + len(good_numbers) + 1))
            score_1 += 2 ** (len(good_numbers) - 1)
        line = f.readline().rstrip()

print('part 1 : ', score_1)
print(len(deck))
