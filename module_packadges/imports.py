import math
from datetime import datetime
from pathlib import Path

print("\nMODULE - IMPORTS")
print("-" * 70)


# Function using imported modules
def calculate_circle_area(radius: float) -> float:
    return math.pi * radius**2


# Example usage
if __name__ == "__main__":
    print(calculate_circle_area(5))
    print("Current time:", datetime.now())

    current_dir = Path.cwd()
    print("Current directory:", current_dir)
    print("Files in current directory:", list(current_dir.iterdir()))
    print("-" * 70)
