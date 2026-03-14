# Another types of characters
# [] = set of characters means what symols are include
# [^] = complementing the set means what symbol not to include

# these above character is replaccement of . because these are more specific than the . one
import re

email = input("What's your email? ").strip()

# Or if re.search(r"^[^@]+@[^@]+\.edu$", email):
if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email): #a-z means a to z and same as for other character
  print("Valid")
else:
  print("Invalid")

# [^@] = means any character except @ sign
# Input: malan@@@harvard.edu
# Output: Invalid
# Input: .edu@something.edu