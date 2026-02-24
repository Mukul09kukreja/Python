# Demonstrates defining a function with a parameter


def hello(to):
    print("hello,", to)


name = input("What's your name? ").strip().title()
hello(name)
