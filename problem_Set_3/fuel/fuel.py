def main():
    while True:
        try:
            fuel = input("Fraction: ").split("/")
            fuel1 = int(fuel[0])
            fuel2 = int(fuel[1])
            fraction(fuel1, fuel2)
            break
        except:
            continue

    

def fraction(a, b):
    while True:
        try:
            if a/b == 1/4:
                print("25%")
                break
            elif a/b == 3/4:
                print("75%")
                break
            elif a/b == 4/4:
                print("F")
                break
            elif a/b == 1/2:
                print("50%")
                break
            elif a == 0:
                print("E")
                break
            
        except ValueError and TypeError:
            continue

main()