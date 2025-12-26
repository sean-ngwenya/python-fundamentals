print("LOOPS & COMPREHENSIONS")
print("-" * 70)

# For loop example
numbers = [1, 2, 3, 4, 5]
print("For loop through numbers:")
for number in numbers:
    print(f" - {number}")

# While loop example
count = 0
print("\nWhile loop counting to 5:")
while count < 5:
    count += 1
    print(f"Count is: {count}")

# List comprehension example
squared_numbers = [x**2 for x in numbers]
print(f"\nSquared numbers using list comprehension: {squared_numbers}")

# Nested loops example
print("\nMultiplication table (1 to 12):")
for i in range(1, 13):
    for j in range(1, 13):
        print(f"{i * j:3}", end=" ")
    print()  # New line after each row
