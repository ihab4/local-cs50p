def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    x, y = fraction.split("/")
    try:
        x, y = int(x), int(y)
        if x <= y:
            return round((x / y) * 100)
    except (ValueError, ZeroDivisionError) as e:
        raise e


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()