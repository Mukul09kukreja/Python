import re

name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):
  name = matches.group(2) + " " + matches.group(1)

print(f"hello, {name}")
''' := it is walrus operator it is new in python 
  and it both allow you to assign a value as i'm doing 
  from right to left.
  and ask a boolean question also
'''