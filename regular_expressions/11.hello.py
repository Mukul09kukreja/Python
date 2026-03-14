# Input: malan@harvard.cs50.edu
# Output: Invalid 
# Reason: because . symbol after @ 
import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
  print("Valid")
else:
  print("Invalid")

# using (...)? here to solve the above problem ? is in 5 no file