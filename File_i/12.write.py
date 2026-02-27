import csv

name = input("What's your name? ")
home = input("Where's your name? ")

with open("File_i/12.write.csv", "a") as file:
  writer = csv.writer(file)
  writer.writerow([ name,home])

# Another way is Dictwriter
import csv

name = input("What's your name? ")
home = input("Where's your name? ")

with open("File_i/12.write.csv", "a") as file:
  writer = csv.DictWriter(file, fieldnames= ["name", "home"])
  writer.writerow({"name": name, "home": home})