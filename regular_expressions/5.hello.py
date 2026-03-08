import re
# re.search(pattern, string, flags=0)
email = input("What's your email? ").strip()

if re.search(".+@.+\.edu", email): #.+ == ..+ means . any character and .* 0 or more chatacter
  print("Valid")
else:
  print("Invalid")

# Pattern forming symbol
# 1. . any character except a newline
# 2. * 0 or more repetation
# 3. + 1 or more repetitions
# 4. ? 0 or 1 repetition
# 5. {m} m repetions
# 6. {m,n} m-n repetitions

# it method read the email left to right where this pattern follow 
# search online for how this pattern run to read 