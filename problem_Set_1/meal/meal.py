def main():
    time = input("What time is it? ").split(":")
    a = int(time[0])
    b = int(time[1])
    print(convert(a, b))

def convert(t1, t2):
    try:
        convert_time1 = t1 * 60
        sum = convert_time1 + t2
        if sum >= 420 and sum <= 480:
            return "breakfast time"
        elif sum >= 1000 and sum <= 1060:
            return "dinner time"
    except:
        return "Invalid Input"

if __name__ == "__main__":
    main()