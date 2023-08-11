due = 50
owed = 0
while due > 0:
    print("Amount Due:", due)
    coin = int(input("Insert Coin: "))
    owed += coin
    if coin == 25 or coin == 10 or coin == 5:
        due -= coin

owed -= 50
print("Change Owed:",owed)

