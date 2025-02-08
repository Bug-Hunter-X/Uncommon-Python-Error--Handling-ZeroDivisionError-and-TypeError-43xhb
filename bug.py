def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Unsupported operand type(s) for /'")
        return None

# Example usage
print(function_with_uncommon_error(10, 2))  # Output: 5.0
print(function_with_uncommon_error(10, 0))  # Output: Error: Division by zero
None
print(function_with_uncommon_error(10, "abc")) # Output: Error: Unsupported operand type(s) for / 
None
print(function_with_uncommon_error(10, 2.5)) # Output: 4.0