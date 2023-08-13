from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fonts:
    figlet.setFont(font= sys.argv[2])
elif len(sys.argv) == 1:
    figlet.setFont(font= random.choice(fonts))
else:
    sys.exit("Invalid usage")

text = input("Input: ")
print("Output:")
print(figlet.renderText(text))

