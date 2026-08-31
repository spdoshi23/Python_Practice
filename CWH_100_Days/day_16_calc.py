x = float(input("Enter first number:  "))
y = float(input("Enter second number:  "))
op = input("Enter any operator among +, -, *, /:  ")

match op:
    case "+":
        print(x+y)
    case "-":
        print(x-y)  
    case "*":
        print(x*y)
    case "/":
        print(x/y)
    case _:
        print("Invalid operator entered")