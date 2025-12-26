# Lists in Python
print("\nDATA STRUCTURES: LISTS")
print("-" * 70)

# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed_list = ["text", 42, 3.14, True]

# Accessing list elements
first_fruit = fruits[0]
last_number = numbers[-1]
print(f"First fruit: {first_fruit}")
print(f"Last number: {last_number}")

# Modifying lists
fruits.append("pineapple")  # Add to the end
fruits.insert(0, "orange")  # Insert at the beginning
numbers.remove(3)  # Remove by value
del fruits[1]  # Remove by index
print(f"Fruits after append: {fruits}")
print(f"Numbers after removal: {numbers}")

# List comprehensions
squared_numbers = [x**2 for x in numbers]  # Square each number in list numbers
print(f"Squared numbers: {squared_numbers}")

# Iterating through lists
print("Fruits in the list:")
for fruit in fruits:
    print(f" - {fruit}")

# List methods
fruits.sort()
print(f"Sorted fruits: {fruits}")
numbers.reverse()
print(f"Reversed numbers: {numbers}")
length_of_mixed_list = len(mixed_list)
print(f"Length of mixed list: {length_of_mixed_list}")
print(
    f"Temporarily sorted list (numbers) {sorted(numbers)}"
)  # Note: does not change the original list

# Slicing lists
subset_of_fruits = fruits[1:3]
print(f"Subset of fruits: {subset_of_fruits}")

# Nested lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print("Matrix:")
for row in matrix:
    print(row)
print(f"Element at row 2, column 3: {matrix[1][2]}")

# List concatenation
combined_list = fruits + numbers
print(f"Combined list: {combined_list}")

# List replication
replicated_list = fruits * 2
print(f"Replicated list: {replicated_list}")

# Checking membership
is_banana_in_fruits = "banana" in fruits
print(f"Is 'banana' in fruits? {is_banana_in_fruits}")

# Clearing a list
mixed_list.clear()
print(f"Mixed list after clearing: {mixed_list}")

# copying a list
copied_fruits = fruits.copy()
print(f"Copied fruits: {copied_fruits}")


# Note: Lists are mutable, meaning their contents can be changed after creation.
