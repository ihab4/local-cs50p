import requests
import sys


try:
    amount = float(sys.argv[1])
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")

r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
bit = r.json()

bpi = bit["bpi"]
curre = bpi["USD"]
price = curre["rate_float"]
price = price * amount


print(f"${price:,.4f}")

