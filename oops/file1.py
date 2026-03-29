def main():
  name, house = get_student()
  print(f"{name} from {house}")

def get_student():
  name = input("Name: ")
  house = input("House: ")
  return (name, house) # here you don't return one value you return a tuple
  # In tuple name and house are two value
if __name__ == "__main__":
  main()