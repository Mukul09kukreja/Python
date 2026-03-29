# Create our owm data sets and gave them names by using classes
# A Class is like a blueprint for pices of data objects 
class Student:
  ...

def main():
  student = get_student() 
  print(f"{student.name} from {student.house}")

def get_student():
  student = Student()
  student.name = input("Name: ")
  student.house = input("House: ")
  return student

if __name__ == "__main__":
  main()

'''
  Objects 
'''