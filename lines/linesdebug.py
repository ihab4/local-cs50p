def main():
    file = open("lines/hello.py")
    code = strip_line(file)
    clean_code = comment_blank(code)
    code_copy = doc_string(clean_code)
    print(len(code_copy))
    file.close()


def strip_line(file):
    code = [line.lstrip() for line in file]
    return code


def comment_blank(code):
    clean_code = [line for line in code if not line.startswith("#") and len(line) != 0]
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


main()