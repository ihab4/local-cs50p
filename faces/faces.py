def convert(text=""):
    text = text.replace(":)", "🙂").replace(":(", "🙁")
    return text

def main():
    user_input = input()
    text = convert(user_input)
    print(text)


main()