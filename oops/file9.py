# Handle Errors in classes
class Student:
  def __init__(self, name, house): # If we want want some parameters optional by using just like house=None
    if not name: # or if name == ""
      raise ValueError("Missing name") # Here we are raise an error and this is good way to handle error for you
    if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
      raise ValueError("Invalid house")
    self.name = name
    self.house = house

def main():
  student = get_student() 
  print(f"{student.name} from {student.house}")

def get_student():
  name = input("Name: ")
  house = input("House: ")
  return Student(name, house)
  

if __name__ == "__main__":
  main()