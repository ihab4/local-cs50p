import csv
from tabulate import tabulate
import sys


def main():
    check_command_line()
    try:
        csvfile = open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File does not exist")
    rows = []
    reader = csv.DictReader(csvfile)
    for row in reader:
        rows.append(row)
    print(rows)
    print(tabulate(rows, headers="keys", tablefmt="grid"))


def check_command_line():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")


main()