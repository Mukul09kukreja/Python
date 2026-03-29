# if you want to change something in tuple make it first in list then change what you want then convert it into tuple
def main():
  student = get_student()
  
  if student[0] == "Padma": 
    student[1] == "Ravenclaw"
    
  print(f"{student[0]} from {student[1]}")

def get_student():
  name = input("Name: ")
  house = input("House: ")
  return [name, house] # change tuple into list

if __name__ == "__main__":
  main()