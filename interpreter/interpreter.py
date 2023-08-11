expression = input("Expression: ").strip()

x, y, z = expression.split(" ")

match y:
    case "+":
        print(float(x) + float(z))
    case "-":
        print(float(x) - float(z))
    case "*":
        print(float(x) * float(z))
    case "/":
        if z != "0":
            print(float(x) / float(z))



