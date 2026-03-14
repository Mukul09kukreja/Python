import re
# re.search(pattern, string, flags=0)
email = input("What's your email? ").strip()

if re.search(r".+@.+\.edu", email): # r use for raw string means this is not escape sequence it pass exactly as it
  print("Valid")
else:
  print("Invalid")

# Input: My email address is mukul@bmu.edu
# Output: Valid
# So here is the problem Like Input: My email id is mukul@bmu.edu
#                             Output: Valid

# Some more symbols
# ^ matches the start of the string
# $ matches ay the end of string or just before the newline at the end of the string