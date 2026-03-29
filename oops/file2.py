# Tuple is the another data type in python
# It is immutable means you can't change the value 
# Tuple --> () is the symbol
def main():
  student = get_student()
  if student[0] == "Padma": # This gives an type error
    student[1] == "Ravenclaw"
  print(f"{student[0]} from {student[1]}")

def get_student():
  name = input("Name: ")
  house = input("House: ")
  return (name, house) 

if __name__ == "__main__":
  main()