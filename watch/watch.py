import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match :=  re.search(r"src=\"(http.+youtube.+/.+/[a-z0-9]+)\"", s, flags=re.IGNORECASE):
        link = match.group(1)
        if link.startswith("http:"):
                link = link.replace("http:", "https:")
        return link.replace("www.", "").replace("be.com/embed", ".be")


if __name__ == "__main__":
    main()
