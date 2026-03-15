'''
A|B either A or B
(...) a group
(?:...) non-capturing version
'''
import re

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)twitter\.com/(.+)$", url, re.IGNORECASE):
  print(f"Username: ", matches.group(1))

#  Another functions:
# re.split(pattern, string, maxsplit=0, flags=0)
# re.findall(pattern, string, flags=0)