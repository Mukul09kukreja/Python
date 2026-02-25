name = input("What's your name? ")

# So here we use with as open file and it automatically
# close the file without any close function
with open("File_i/5.names.txt", "a") as file:
  file.write(f"{name}\n")

# So here we read the file
# Method 1
with open("File_i/5.names.txt", "r") as file1:
  lines = file1.readlines()

for line in lines:
  print("hello,", line.rstrip())

# Method 2
with open("File_i/5.names.txt") as file:
  for line in file:
    print("hello", line.rstrip())