def function_with_improved_error_handling(a, b):
    try:
        if not isinstance(b, (int, float)):
            raise TypeError("Divisor must be a number")
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        result = a / b
        return result
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")
        return None
    except TypeError as e:
        print(f"TypeError: {e}")
        return None

# Example usage
print(function_with_improved_error_handling(10, 2))  # Output: 5.0
print(function_with_improved_error_handling(10, 0))  # Output: ZeroDivisionError: Division by zero
None
print(function_with_improved_error_handling(10, "abc")) # Output: TypeError: Divisor must be a number
None
print(function_with_improved_error_handling(10, 2.5)) # Output: 4.0