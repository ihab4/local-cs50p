months = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November","December"
]

def main():
    year, month, day = get_date()
    print(f"{year}-{month:02}-{day:02}")

def get_date():
    while True:
        date = input("Date: ").title()
        try:
            month, day, year = date.split("/")
            year, month, day = int(year), int(month), int(day)
        except ValueError:
            try:
                month_day, year = date.split(",")
                month, day = month_day.split()
                month = months.index(month) + 1
            except ValueError:
                continue

        if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
            return int(year), int(month), int(day)

main()
