class Hand():
    RANKS = ['Five of a kind',
             'Four of a kind',
             'Full house',
             'Three of a kind',
             'Two pair',
             'One pair',
             'High card']
    
    def __init__(self, line, bid, part = 1):

        self.part = part
        self.cards = line
        self.hand_type = self.get_hand_type()
        self.bid = int(bid)

    def __gt__(self, hand):
        ranks = self.RANKS
        if self.part == 1:
            card_ranks = 'AKQJT98765432'
        else:
            card_ranks = 'AKQT98765432J'
            
        if ranks.index(self.hand_type) == ranks.index(hand.hand_type):
            pile_self = self.cards
            pile_other = hand.cards
            
            while pile_self != '':
                if (card_ranks.index(pile_self[0]) ==
                    card_ranks.index(pile_other[0])):
                    pile_self = pile_self[1:]
                    pile_other = pile_other[1:]
                else:
                    return (card_ranks.index(pile_self[0])
                            > card_ranks.index(pile_other[0]))
                    
        else:
            return ranks.index(self.hand_type) > ranks.index(hand.hand_type)

    def __repr__(self):
        return f'{self.cards} : {self.bid}'

    def get_hand_type(self):
        counter = {}
        card_hand = self.cards
        for card in card_hand:
            if card not in counter.keys():
                counter[card] = 1
            else:
                counter[card] += 1

        if self.part == 2:
            if 'J' in counter.keys():
                count_joker = counter['J']
                del counter['J']
            else:
                count_joker = 0

            if count_joker == 5:
                return 'Five of a kind'

            maximum_num_card = max(counter.values())
            for key, val in counter.items():
                if val == maximum_num_card:
                    card_hand = card_hand.replace('J', key)
                    counter[key] += count_joker
                    break

            
        if len(set(card_hand)) == 1:
            return 'Five of a kind'
        elif len(set(card_hand)) == 2:
            if max(counter.values()) == 4:
                return 'Four of a kind'
            else:
                return 'Full house'
        elif len(set(card_hand)) == 3:
            if max(counter.values()) == 2:
                return 'Two pair'
            else:
                return 'Three of a kind'                
        elif len(set(card_hand)) == 4:
            return 'One pair'
        else:
            return 'High card'

data_1 = []
data_2 = []
with open('input') as f:
    line = f.readline().rstrip()

    while line != '':
        hand, bid = line.split(' ')
        data_1.append(Hand(hand, bid, part = 1))
        data_2.append(Hand(hand, bid, part = 2))        

        line = f.readline().rstrip()

data_1.sort(reverse = True)
data_2.sort(reverse = True)

score_1 = [(i + 1) * hand.bid for i, hand in enumerate(data_1)]
score_2 = [(i + 1) * hand.bid for i, hand in enumerate(data_2)] 
print('part 1 : ', sum(score_1))
print('part 2 : ', sum(score_2))
        
        
    
