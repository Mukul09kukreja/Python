def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")
    print(check(answer))

def check(answer):
    # Strip whitespace and convert to lowercase for comparison
    answer = answer.strip().lower()
    
    if answer in ("42", "forty-two", "forty two"):
        return "Yes"
    else:
        return "No"

main()