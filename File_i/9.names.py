# Here we learn about sorting of dictionary
# Using 8.names.csv file here to learn sorting dictionary
students = []
with open("File_i/8.names.csv") as file:
  for line in file:
    name, place = line.rstrip().split(",")
    student = {"name": name, "place": place}
    students.append(student)
def get_name(student):
  return student["name"]

for student in sorted(students, key=get_name): #Here sorted by key value in the list and nested dictionary
  print(f"{student['name']} is in {student['place']}")

# LAMDA function
''' lamda function is using here to remove def get_name function
  1. lambda is anonymous function without name
  2. lambda syntax is lambda parameter: return_value
'''
for student in sorted(students, key=lambda student: student["name"]):
  print(f"{student['name']} is in {student['place']}")