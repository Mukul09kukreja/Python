# Methods and functions inside of classes
# 1. Instance Methods: __init__ method
class Student:
  # Always calling function below one
  def __init__(self, name, house): # Method use to define objects in classes
    self.name = name
    self.house = house

def main():
  student = get_student() 
  print(f"{student.name} from {student.house}")

def get_student():
  name = input("Name: ")
  house = input("House: ")
  student = Student(name, house) # This is generally known as  constructor cell
  return student

if __name__ == "__main__":
  main()