name = input("camelCase: ")
snake = ""
for c in name:
    if c.isupper():
        c = "_" + c.lower()
    snake += c

print("snake_case:",snake)