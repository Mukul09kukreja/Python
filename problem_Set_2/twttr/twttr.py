def main():
    line = input("Input: ")
    print(change(line))

def change(phrase):
    vowel = ["a", "e", "i", "o", "u"]
    for i in vowel:
        phrase = phrase.lower().replace(i, "")

    phrase = str(phrase)
    return f"Output: {phrase.capitalize()}"

main()