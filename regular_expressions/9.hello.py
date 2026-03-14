import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.(edu|com|net|gov)$", email): # use list in it re .(com|edu|net|org)
  print("Valid")
else:
  print("Invalid")

# \w = wordcase character known for alphanumeric symbol or underscore
# \d = decimal digit
# \D = not a decimal digit
# \s = whitespace characters
# \S = not a whitespace character
# \w = word character as well as numbers and underscore
# \W = not a word character

# A|B = either A or B
# (...) = a group
# (?:...) = non capturing version