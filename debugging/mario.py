def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print("#"* (i + 1))
    #Removal of j loop in above code

if __name__ == "__main__":
    main()