import inflect

p = inflect.engine()
names = list()

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        break

print("Adieu, adieu, to", p.join(names))

