# In this file we store names
name = input("What's your name? ")
print(f"hello, {name}")

# if i want to store more than one name use lists
names = []
for _ in range(3):
  names.append(input("What's your name? "))

print(sorted(names)) #sorted used to sort the list by their order