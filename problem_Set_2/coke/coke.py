def main():
    amount = 50
    print(check(amount))

def check(amount):
    while amount > 0:
        print(f"Amount Due: {amount}")
        try:
            minus = int(input("Insert coin: "))
        except ValueError:
            continue
        else:
            amount = amount - minus

    if amount == 0:
        return "Change Owned: 0"
    else:
        return f"Change owned: {str(amount).replace("-", "")}"

main()