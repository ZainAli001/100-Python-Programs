import random,itertools


deck  = list(itertools.product(range(1,14),["DIAMOND","SPADE","CLUB","HEART"]))
# print(deck)
random.shuffle(deck)
# print(deck)

for i in range(5):
    print(deck[i][0],deck[i][1])