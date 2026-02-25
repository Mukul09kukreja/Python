# So here we larn how to sort another file 
names = [] 
with open("File_i/6.names.txt", "r") as file:
  for line in file:
    names.append(line.rstrip())

for _ in sorted(names):
  print(f"{_}")

# So here we first make a list append items in it then sorted and print by using loops
# Easy way to do
with open("File_i/6.names.txt") as file1:
  for line1 in sorted(file1):
    print(f"{line1.rstrip()}")

# How to change the order of sorting by own?
# Ans: Use documentation  you see like this 
#      sorted(iterable, /,*, Key=None, reverse=False)
# Ex:
with open("File_i/6.names.txt") as file2:
  for line2 in sorted(file2, reverse=True):
    print(f"{line2.rstrip()}")