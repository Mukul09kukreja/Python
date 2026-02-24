# Demonstrates str functions

name = input("What's your name? ").strip().title()
first, last = name.split(" ")
print(f"hello, {first}")
print(f"Surname {last}")
#.split use for seperate the one string into two string 