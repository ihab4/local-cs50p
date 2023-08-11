grocery = dict()

while True:
    try:
        item = input().strip().upper()
    except EOFError:
        print()
        break
    grocery[item] = grocery.get(item, 0) + 1

for k, v in sorted(grocery.items()):
    print(v, k)
