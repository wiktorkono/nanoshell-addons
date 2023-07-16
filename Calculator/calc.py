def calculate(expression):
    expression = expression.replace("calc ", "")
    try:
        print(eval(expression))
    except (SyntaxError, NameError, TypeError) as e:
        print("Invalid expression: " + str(e))
    except ZeroDivisionError:
        print("Division by zero is not allowed. ")