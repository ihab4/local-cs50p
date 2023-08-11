def main():
    time = input("What time is it? ")
    time = convert(time)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    if time.endswith("a.m."):
        time = time.strip("a.m.")
    elif time.endswith("p.m."):
        time = time.strip("p.m.")
        hour, minute = time.split(":")
        hour = int(hour) + 12
        time = str(hour) + ":" + minute

    hour, minute = time.split(":")
    minute = int(minute) / 60
    time = int(hour) + minute
    return time


if __name__ == "__main__":
    main()