def main():
    word = input("Input: ")
    print("Output:", shorten(word))


def shorten(word):
    vowel = ["a", "e", "i", "o", "u"]
    omitted = ""
    for c in word:
        if c.lower() not in vowel:
            omitted += c
    return omitted


if __name__ == "__main__":
    main()