# math_operations.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

# def divide(x, y):
#     if y != 0:
#         return x / y
#     else:
#         return "Error: Division by zero!"


def divide(x, y):
    try:
        result = x / y
        return result
    except Exception as e:
        print(f"Error in divide() from math_operations_module : {e}")
        raise


