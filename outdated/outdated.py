months = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November","December"
]

def main():
    year, month, day = get_date()
    print(f"{year}-{month:02}-{day:02}")

def get_date():
    while True:
        date = input("Date: ")
        try:
            month, day, year = date.split("/")
            year, month, day = int(year), int(month), int(day)
            if 1 <= month <= 12 and 1 <= day <= 31:
                return year, month, day
        except ValueError:
            try:
                month_day, year = date.split(",")
                month, day = month_day.split()
                month = months.index(month) + 1
                year, month, day = int(year), int(month), int(day)
                if 1 <= month <= 12 and 1 <= day <= 31:
                    return year, month, day
            except ValueError:
                pass

main()
