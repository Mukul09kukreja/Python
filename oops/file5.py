# Create our owm data sets and gave them names by using classes
# A Class is like a blueprint for pices of data objects 
class Student:
  ...

def main():
  student = get_student() 
  print(f"{student.name} from {student.house}")

def get_student():
  student = Student() # student is an object of class
  student.name = input("Name: ") # it is beecome new dataset
  student.house = input("House: ") # it is beecome new dataset
  return student

if __name__ == "__main__":
  main()

# Objects is use of classes, it is mutable
# Name, house is an attributes of class Student and this is also called instance variables
# Ex: name, house it is a variable inside class