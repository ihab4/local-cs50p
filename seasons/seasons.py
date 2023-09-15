from datetime import date
import inflect
import sys


def main():
    try:
        birth = date.fromisoformat(input("Date fo birth: "))
    except ValueError:
        sys.exit("Invalid date")
    int_minutes = calcul(birth)
    print(convert_minutes(int_minutes))


def calcul(birth):
    return (date.today() - birth).days * 24 * 60


def convert_minutes(minutes):
    p = inflect.engine()
    return (p.number_to_words(minutes, andword="") + " minutes").capitalize()


if __name__ == "__main__":
    main()