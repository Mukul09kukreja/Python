students = []
with open("File_i/10.csv_lib.csv") as file:
  for line in file:
    name, home = line.rstrip().split(",")
    student = {"name": name, "home": home}
    students.append(student)

for student in sorted(students, key=lambda student: student["name"]):
  print(f"{student['name']} is in {student['home']}")

# if we face the problem of storing data in csv that had 3 commas but you read 2 in it 
# then use csv library for it 
import csv

studentsp = []
with open("File_i/10.csv_lib.csv") as filep:
  reader = csv.reader(filep)
  for name0, home0 in reader:
    studentsp.append({"name": name0, "home": home0})

for student in sorted(studentsp, key=lambda student: student["name"]):
  print(f"{student['name']} is in {student['home']}")