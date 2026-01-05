def main():
    expression = input("Expression: ")
    print(check(expression))


def check(expression):
    try:
        if "+" in expression:
            a = expression.replace("+", "")
            a1 = float(a[0])
            a2 = float(a[1])
            sum = a1 + a2
            return sum
        elif "-" in expression:
            a = expression.replace("-", "")
            a1 = float(a[0])
            a2 = float(a[1])
            subtraction = a1 - a2
            return subtraction
        elif "*" in expression:
            a = expression.replace("*", "")
            a1 = float(a[0])
            a2 = float(a[1])
            multiplication = a1 * a2
            return multiplication
        else:
            a = expression.replace("*", "")
            a1 = float(a[0])
            a2 = float(a[1])
            division = a1 * a2
            return division
    except ValueError:
        return "Invalid input"

main()