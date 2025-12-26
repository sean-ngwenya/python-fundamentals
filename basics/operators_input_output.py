# This script takes two numbers as input from the user,# performs basic arithmetic operations (addition, multiplication,
# division, and subtraction), and prints the results.

# ============================================================================
# 2. OPERATORS & INPUT/OUTPUT
# ============================================================================
print("\n2. OPERATORS & INPUT/OUTPUT")
print("-" * 70)
# Take two numbers as input from the user
number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))

# Perform arithmetic operations
sum_result = number_1 + number_2
product_result = number_1 * number_2
quotient_result = number_1 / number_2
difference_result = number_1 - number_2
floor_division_result = number_1 // number_2
squared_result = number_1**2


# Output the results
print(f"\n{number_1} + {number_2} = {sum_result}")
print(f"{number_1} * {number_2} = {product_result}")
print(f"{number_1} divided by {number_2} = {quotient_result}")
print(
    f"The difference when {number_2} is subtracted from {number_1} is: {difference_result}"
)
print(f"The floor division of {number_1} by {number_2} is: {floor_division_result}")
print(f"The square of {number_1} is: {squared_result}")

# Note: Ensure to handle division by zero in a real-world scenario.

# Using comparison operators
if number_1 == number_2:
    print(f"\n{number_1} is equal to {number_2}")
elif number_1 > number_2:
    print(f"\n{number_1} is greater than {number_2}")
else:
    print(f"\n{number_1} is less than {number_2}")

if number_1 % 2 == 0:
    print(f"{number_1} is an even number.")

if number_1 % 2 != 0:
    print(f"{number_1} is an odd number.")

# Using nested conditionals
has_license = True
is_drunk = False

if has_license:
    if not is_drunk:
        print("You can drive.")
    else:
        print("You cannot drive while drunk.")
else:
    print("You need a license to drive.")

# Using logical operators
if has_license and not is_drunk:
    print("You can drive.")

if not has_license or is_drunk:
    print("You cannot drive.")

# ============================================================================
