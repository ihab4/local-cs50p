import sys


def main():
    check_command_line()
    try:
        file = open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File does not exist")
    count = 0 
    for line in file:
        if not line.isspace() and not line.lstrip().startswith("#"):
            count += 1
    print(count)


def check_command_line():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a python file")


main()