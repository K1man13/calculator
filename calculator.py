def calculator():
    try:
        num1 = 13
        num2 = 10

        operation = '*'

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Invalid operation. Please enter +, -, *, or /.")
            return

        print(f"{num1} {operation} {num2} = {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")



calculator()
