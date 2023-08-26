import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1].endswith(".py"):
            try:
                file = open(sys.argv[1])
            except FileNotFoundError:
                sys.exit("File does not exist")

            code = [line.lstrip() for line in file]
            clean_code = [line for line in code if not line.startswith("#") and len(line) != 0]
            code_copy = doc_string(clean_code)
            print(len(code_copy))
            file.close()
        else:
            sys.exit("Not a python file")


def doc_string(clean_code):
    code_copy = clean_code
    for index, line in enumerate(clean_code):
        if line.startswith('"""'):
            for l in clean_code[index+1:]:
                code_copy.pop(index)
                if l.endswith('""\n'):
                    code_copy.pop(index)
                    break
    return code_copy


main()