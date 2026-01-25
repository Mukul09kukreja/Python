import random

cards = ["jack", "queen", "king"]


def main():
    output = random.sample(cards, k=2)
    print(output)


main()
