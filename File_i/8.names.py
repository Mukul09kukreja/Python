# This program is upgraded version of previous one 
with open("File_i/7.names.csv") as file:
  for line in file:
    name,place = line.rstrip().split(",")
    print(f"{name} is in {place}")

# Now I want to sorted this code 
students = []
with open("File_i/8.names.csv") as file:
  for line in file:
    name, place = line.rstrip().split(",")
    students.append(f"{name} is in {place}")

for student in sorted(students):
  print(student)

# By using dictionary to print csv file
studentsp = []
with open("File_i/8.names.csv") as file1:
  for line1 in file1:
    name1, place1 = line1.rstrip().split(",")
    studentp = {"name": name1, "place": place1}
    studentsp.append(studentp)

for studentp in studentsp:
  print(f"{studentp['name']} is in {studentp['place']}")