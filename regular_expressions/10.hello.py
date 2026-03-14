# Input: MALAN@HARVARD.EDU
# Output: Invalid 
# so we use email = input(...).strip().lower()
# Instesd of using lower we can use flags 
# re.search(pattern, string, flags=0)
import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.(edu|com|net|gov)$", email, re.IGNORECASE): # if i use flags= re.IGNORECASE we can use it any direction
  print("Valid")
else:
  print("Invalid")

# re build in search function\
# re.IGNORECASE = ignore all casses like upercase or lowercase or any tyoe of cases
# re.MULTILINE = handle multiple lines span
# re.DOTALL = handle match character in string to row string