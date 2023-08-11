def main():
    fra = get_fraction()
    if fra <= 0.01:
        print("E")
    elif fra >= 0.99:
        print("F")
    else:
        print(f"{round(fra * 100)}%")


def get_fraction():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            x, y = int(x), int(y)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            if x <= y:
                return x / y


main()