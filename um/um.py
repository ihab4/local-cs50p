import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    match = re.findall(r"\bum\b", s, flags=re.IGNORECASE)
    if match:
        return len(match)
    else:
        return 0



if __name__ == "__main__":
    main()