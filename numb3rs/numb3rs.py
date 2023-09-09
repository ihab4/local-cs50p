import re
# import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.search(r"^(?:(?:[0-1]?[0-9]?[0-9]?|2(?:[0-4][0-9]|5[0-5]))\.){3}(?:[0-1]?[0-9]?[0-9]?|2(?:[0-4][0-9]|5[0-5]))$", ip)
    if match:
        return True
    else:
        return False


if __name__ == "__main__":
    main()