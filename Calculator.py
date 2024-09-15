import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b

def power(a, b):
    return a ** b

def sqrt(a):
    if a < 0:
        raise ValueError("Cannot calculate the square root of a negative number!")
    return math.sqrt(a)

# Function to evaluate expressions
def evaluate(expression):
    try:
        # Evaluating the expression safely using Python's eval()
        result = eval(expression, {"__builtins__": None}, {"sqrt": sqrt, "pow": power, "math": math})
        return result
    except ZeroDivisionError as e:
        return f"Error: {e}"
    except ValueError as e:
        return f"Error: {e}"
    except Exception:
        return "Error: Invalid input or malformed expression"

def main():
    print("""Welcome to the Simple Calculator
You can perform operations like +, -, *, /, ^(exponent), sqrt, and use parentheses.
Example: (2+3)*4^2 or sqrt(16)""")

    while True:
        user = input("Enter your expression (or 'exit' to quit): ").replace(' ','')
        
        if user.lower() == 'exit':
            print("Exiting calculator.")
            break
        
        result = evaluate(user)
        print(f"Result: {result}")

#main function
main()
