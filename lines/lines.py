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

            code = strip_line(file)
            clean_code = comment_blank(code)
            code_copy = doc_string(clean_code)
            print(len(code_copy))
            file.close()
        else:
            sys.exit("Not a python file")


def strip_line(file):
    code = []
    for line in file:
        code.append(line.lstrip())
    return code


def comment_blank(code):
    clean_code = []
    for line in code:
        if not line.startswith("#") and len(line) != 0:
            clean_code.append(line)
    return clean_code


def doc_string(clean_code):
    code_copy = clean_code
    for index, line in enumerate(clean_code):
        if line.startswith('"""\n'):
            for l in clean_code[index+1:]:
                code_copy.pop(index)
                if l.endswith('""\n'):
                    code_copy.pop(index)
                    break
        elif line.startswith('"""'):
            doc = []
            for l in clean_code[index:]:
                doc.append(l)
                if l.endswith('"""\n'):
                    for elmnt in doc:
                        code_copy.remove(elmnt)
                    break


    return code_copy
    # doc = []
    # for index, start in enumerate(clean_code):
    #     if start != '"""\n':
    #         ind = []
    #         if start.startswith('"""'):
    #             doc.append(start)
    #             ind.append(index)
    #             if start.endswith('"""\n'):
    #                 return code_copy.pop(ind)

    #     else:
    #         if start.startswith('"""\n'):
    #             for l in clean_code[index+1:]:
    #                 code_copy.pop(index)
    #                 if l.endswith('""\n'):
    #                     code_copy.pop(index)
    #                     return code_copy


main()