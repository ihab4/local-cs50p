import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.search(r"([0-9]|1[0-2]):?([0-5][0-9])? (AM|PM) to ([0-9]|1[0-2]):?([0-5][0-9])? (AM|PM)", s)
    if match:
        start_hr = int(match.group(1))
        if start_hr == 12:
            start_hr = 0
        if match.group(2) != None:
            start_min = match.group(2)
        else:
            start_min = "00"
        if match.group(3) == "PM":
            start_time = ":".join([f"{start_hr+12:02}", start_min])
        else:
            start_time = ":".join([f"{start_hr:02}", start_min])

        end_hr = int(match.group(4))
        if end_hr == 12:
            end_hr = 0
        if match.group(5) != None:
            end_min = match.group(5)
        else:
            end_min = "00"
        if match.group(6) == "PM":
            end_time = ":".join([f"{end_hr+12:02}", end_min])
        else:
            end_time = ":".join([f"{end_hr:02}", end_min])

        return f"{start_time} to {end_time}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()