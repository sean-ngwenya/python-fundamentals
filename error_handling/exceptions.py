print("\nERROR HANDLING - EXCEPTIONS")
print("-" * 70)


# Function demonstrating exception handling
def divide(a: float, b: float) -> float:
    try:
        result = a / b
    except ZeroDivisionError:  # Handle division by zero
        raise ValueError("Division by zero is not allowed")
    except TypeError:  # Handle invalid input types
        raise TypeError("Inputs must be numbers")
    else:
        return result
    finally:
        print("Execution completed")


# Example usage
if __name__ == "__main__":
    try:
        print(divide(10, 2))
        print(divide(10, 0))
    except Exception as e:
        print(f"Error: {e}")
