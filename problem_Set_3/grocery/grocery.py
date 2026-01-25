def main():
    try:
        grocery = []
        while True:
            item = input().capitalize()
            grocery.append(item)
    except EOFError and KeyboardInterrupt:
        for ppt in grocery:
            count = grocery.count(ppt)
            print(f"{count} {ppt}")

if __name__ == "__main__":
    main()