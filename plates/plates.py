def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 < len(s) <= 6 and s[:2].isalpha():
        new_s = s[2:]
        if new_s.isalpha():
            return True
        for index, c in enumerate(new_s):
            if not c.isalpha():
                ss = new_s[index:]
                break
        if ss.isdecimal() and not(ss.startswith("0")):
            return True
        else:
            return False
    else:
        return False

main()
