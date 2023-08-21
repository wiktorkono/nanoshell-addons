def calculate(expression):
    expression = expression.replace("calc ", "")
    try:
        print(eval(expression))
    except (SyntaxError, NameError, TypeError) as e:
        print(f"Invalid expression: {e}")
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
