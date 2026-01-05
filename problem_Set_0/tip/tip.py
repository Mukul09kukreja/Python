def main():
    while True:
        try:
            cost = input("How much for the meal? ").replace("$", "")
            cost1 = float(cost)
            tip_percent = input("What percentage would you like to tip? ").replace("%", "")
            tip_percent1 = float(tip_percent)
        except ValueError:
            continue
        else:
            print(f"Leave ${calculate(cost1, tip_percent1)}")
            break

def calculate(m, n):
    leave = m * (n/100)
    return leave

main()