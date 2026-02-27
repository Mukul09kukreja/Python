# Like if you want like add title coloumn in csv and then access you can do this by using DictReader
import csv

students = []
with open("File_i/11.Dictreader.csv") as file:
  reader = csv.DictReader(file)
  for row in reader:
    students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
  print(f"{student['name']} is in {student['home']}")

# if i want to change the rows
# specif Note: change header acc to changing row data