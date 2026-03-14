''' if user input not same as re so we need to clean up from csv manually that had an headache for us instead of cleaning 
manually we can code in python is more efffective''' 
# So here our goal is to reformat the user input in the format we except
name = input("What's your name? ").strip()
if "," in name:
  last, first = name.split(", ")
  name = f"{first} {last}"
print(f"hello, {name}")
'''Input: malan, david
  Output: hello, malan, david
'''