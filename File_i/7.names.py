# So If i want to add more than than names in txt file
# How to do it? 
# Ans: So here we discuss about this how to store and use
#      So here we use csv file instead of txt file to store data like excel or spreadshets

# First we gonna read a csv file:
with open("File_i/7.names.csv") as file:
  for line in file:
    row = line.rstrip().split(",")
    print(f"{row[0]} is in {row[1]}")