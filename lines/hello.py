# Say hello
#hi

name = input("What's your name? ")
print(f"hello, {name}")



def main():

    """this is
    a doc abc"""
    fra = get_fraction()
    if fra <= 0.01:
        print("E")
    elif fra >= 0.99:
        print("F")
    else:
        print(f"{round(fra * 100)}%")

main()