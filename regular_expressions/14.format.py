import re

name = input("What's your name? ").strip()
# here we used grouped together = (...) it is a group
matches = re.search(r"^(.+), *(.+)$", name)
if matches:
  name = matches.group(2) + " " + matches.group(1)

print(f"hello, {name}")