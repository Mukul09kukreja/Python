# regular expressions or regexes is pattern that use in python to match data
# user email address
email = input("What's your email? ").strip()

if "@" in email:
  print("Valid")
else:
  print("Invalid")