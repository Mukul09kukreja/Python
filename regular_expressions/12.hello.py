# What regular expression use in browser validation
# We will see in this file
import re

email = input("What's your email? ").strip()

if re.search(r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", email): # So this is re of web email validation
  print("Valid")
else:
  print("Invalid")

# Another functions in re library
# re.match(pattern, string, flags=0)
