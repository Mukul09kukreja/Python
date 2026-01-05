def main():
    while True:
        try:
            m = int(input("m: "))
        except ValueError:
            continue
        else:
            print(calculate(m))
            break

def calculate(m):
    c = 300000000
    e = m * c**2
    return e

main()