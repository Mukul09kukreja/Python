import random

pick = ["Head", "Tail"]

flip = random.choice(pick)

number = random.randint(1, 10)
print(f"flip face: {flip}")
print(number)

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)