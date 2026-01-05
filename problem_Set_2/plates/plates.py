def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    phrase = []
    for i in s:
        phrase.append(i)

    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    
    if (phrase[0] or phrase[1]) != numbers:
        if (phrase[2] or phrase[3]) != numbers:
            return True
    else:
        return False
    
    for i in phrase:
        if i == (":" or "," or "_"):
            return False


main()