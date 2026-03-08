email = input("What's your email? ").strip()

username, domain = email.split("@")

if username and domain.endswith(".edu"):
  print("Valid")
else:
  print("Invalid")

# Input: mukul@.edu
# Output: Valid
# So how to solve the problem instead of write a lot of code 
# re it is a library to use to solve this kind of problem