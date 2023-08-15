import random


def main():
    level = get_level()  
    score = 0
    for _ in range(10):
        wrong = 0
        num1, num2 = generate_integer(level)
        while wrong != 3:
            try:
                answer = int(input(f"{num1} + {num2} = "))
            except ValueError:
                continue
            if answer == (num1 + num2) or wrong == 3:
                break
            else:
                print("EEE")
                wrong += 1
        if wrong == 3:
            print(f"{num1} + {num2} = {num1 + num2}")
            score -= 1 
        score += 1

    print("Score:", score)



def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <=3:
                return level
        except ValueError:
            pass                



def generate_integer(level):
    if level == 1:
        num1 = random.randint(0,9)
        num2 = random.randint(0,9)
    elif level == 2:
        num1 = random.randint(10,99)
        num2 = random.randint(10,99)
    else:
        num1 = random.randint(100,999)
        num2 = random.randint(100,999)

    return num1, num2



if __name__ == "__main__":
    main()




