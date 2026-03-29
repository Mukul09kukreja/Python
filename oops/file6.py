class Student:
  ...

def main():
  student = get_student() 
  print(f"{student.name} from {student.house}")

def get_student():
  name = input("Name: ")
  house = input("House: ")
  student = Student(name, house) # By using this we can handle error in it 
  return student

if __name__ == "__main__":
  main()