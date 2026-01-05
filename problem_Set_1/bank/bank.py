def main():
    phrase = input("Greeting: ")
    print(message(phrase))


def message(phrase):
    try:
        if "Hello" in phrase:
            return "0$"
        elif ("Hey" or "How") in phrase:
            return "20$"
        elif "What" in phrase:
            return "100$"
        else:
            return "No money"
    except:
        return "Invalid output"


main()