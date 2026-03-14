# Another types of characters
# [] = set of characters
# [^] = complementing the set

# these above character is replaccement of . because these are more specific than the . one
import re

email = input("What's your email? ").strip()

if re.search(r"^[^@]+@[^@]+\.edu$", email):
  print("Valid")
else:
  print("Invalid")

# [^@] = means any character except @ sign
# Input: malan@@@harvard.edu
# Output: Invalid