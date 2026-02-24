# Compares multiple strings
answer = input("Do you agree? ").strip().lower()
if answer == "yes" or answer == "y":
    print("Agreed")
else:
    print("Not agreed")

#This is additional code that i made just for fun
while True:
    answer = input("Do you agree? ").strip().lower()
    if answer == "yes" or answer == "y":
        print("Agreed")
        break
    elif answer == "no" or answer == "n":
        print("Not agreed")
        break
    else:
        continue