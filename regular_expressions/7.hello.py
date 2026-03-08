import re

email = input("What's your email? ").strip()

if re.search(r"^.+@.+\.edu$", email):
  print("Valid")
else:
  print("Invalid")

# Input: My email is mukul@bmu.edu.
# Output: Invalid

# so here start and end component of re library fix the previous problem

# Input: mukul@@@bmu.edu.
# Output: Valid
# How to fix this in next file 