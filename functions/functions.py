#
print("\nFUNCTIONS")
print("-" * 70)


# Simple function definitions and usage
def greet(name, greeting="Hello"):
    """Simple greeting function"""
    return f"{greeting}, {name}!"


def calculate_stats(numbers):
    """Calculate basic statistics"""
    return {
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "count": len(numbers),
    }


# Example usage
print(greet("World"))
print(greet("Python", "Welcome"))

data = [10, 20, 30, 40, 50]
stats = calculate_stats(data)

print(f"\nStatistics for {data}:")

for key, value in stats.items():
    print(f"  {key}: {value}")
