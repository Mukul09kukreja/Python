import sys
from pyfiglet import Figlet
f = Figlet(font=sys.argv[2])
print(f"output: {f.renderText(input("Input: "))}")