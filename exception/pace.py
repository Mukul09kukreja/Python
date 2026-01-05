def main():
    miles = float(input("Enter miles: "))
    minutes = float(input("Enter minutes: "))
    pace = get_pace(miles, minutes)
    print(f"You need to run each mile in {round(pace, 2)} minutes.")

def get_pace(miles, minutes):
    if not minutes > 0:
        raise ValueError("Invalid Value for minutes")

    return minutes/miles


main()