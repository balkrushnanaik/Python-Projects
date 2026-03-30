print("Welcome to the calculator")
num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))

oper = input("Enter operator: ")

match oper:
    case "+":
        print(f"Addition of {num1} and {num2} is {num1+num2}")
    case "-":
        print(f"Subtraction of {num1} and {num2} is {num1-num2}")
    case "*":
        print(f"Multiplication of {num1} and {num2} is {num1*num2}")
    case "/":
        print(f"Division of {num1} and {num2} is {num1/num2}")
    case "**":
        print(f"Power of {num1} and {num2} is {num1**num2}")
    case "%":
        print(f"Remainder of {num1} and {num2} is {num1%num2}")
    case _:
        print(f"Operator {oper} is invalid")