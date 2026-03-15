import re

url = input("URL: ").strip()
# Another function is re.sub(pattern, repl, string, count=0, flags=0)
# repl means replacement string 
username = re.sub(r"^(https?://)?(www\.|)?twitter\.com/", "", url)

'''Input: https:\\www.google.com\
  Output: https:\\www.google.com\
  This is the problem
'''