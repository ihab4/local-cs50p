from PIL import Image, ImageOps
import sys
import os


def main():
    check_commande_line()
    try:
        photo = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")    
    shirt = Image.open("shirt.png")
    new = ImageOps.fit(photo, shirt.size)
    new.paste(shirt, shirt)
    new.save(sys.argv[2])

def check_commande_line():
    
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    
    if not (sys.argv[2].endswith(".jpeg") or sys.argv[2].endswith(".jpg") or sys.argv[2].endswith(".png")):
        sys.exit("Invalid output")
    elif os.path.splitext(sys.argv[1])[1] != os.path.splitext(sys.argv[2])[1]:
        sys.exit("Input and output have different extensions")


main()