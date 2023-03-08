def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs') from e
    else:
        return result

try:
    divide(5, 0)
except ValueError as e:
    print("Cause of error:", e.__cause__)
    print(type(e.__cause__))

# Cause of error: division by zero
# <class 'ZeroDivisionError'>