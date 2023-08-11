text = input("Input: ")

vowel = ["a", "e", "i", "o", "u"]
omitted = ""
for c in text:
    if c.lower() not in vowel:
        omitted += c

print("Output:", omitted)
