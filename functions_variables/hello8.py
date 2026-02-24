# Demonstrates defining a function without parameters


def hello():
    return "hello"


name = input("What's your name? ")
hello()
print(name)
print(f"{hello} {name}") # hello gives their address where it store
print(hello(), name)