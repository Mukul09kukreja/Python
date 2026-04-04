class Student:
  ...

def main():
  student = get_student() 
  print(f"{student.name} from {student.house}")

def get_student():
  name = input("Name: ")
  house = input("House: ")
  student = Student(name, house) # takes no arguments but from here we learned learn more powerful tools in Student and 
  # It later handle validation and error of validation or type error
  return student

if __name__ == "__main__":
  main()