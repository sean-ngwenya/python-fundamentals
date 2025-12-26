print("\n DATA STRUCTURES: SETS")
print("-" * 70)

# Creating sets
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
mixed_set = {"text", 42, 3.14, True}

# Accessing set elements
print(f"Fruits set: {fruits}")
print(f"Numbers set: {numbers}")

# Modifying sets
fruits.add("orange")  # Add an element
numbers.discard(3)  # Remove an element if it exists
print(f"Fruits after adding orange: {fruits}")
print(f"Numbers after discarding 3: {numbers}")

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
union_set = set_a.union(set_b)
intersection_set = set_a.intersection(set_b)
difference_set = set_a.difference(set_b)
print(f"Union of set_a and set_b: {union_set}")
print(f"Intersection of set_a and set_b: {intersection_set}")
print(f"Difference of set_a and set_b (set_a - set_b): {difference_set}")

# Iterating through sets
print("Fruits in the set:")
for fruit in fruits:
    print(f" - {fruit}")

# Set methods
is_subset = {1, 2}.issubset(set_a)
is_superset = set_a.issuperset({1, 2})
print(f"Is {{1, 2}} a subset of set_a? {is_subset}")
print(f"Is set_a a superset of {{1, 2}}? {is_superset}")

# Note: Sets are unordered collections, so elements may appear in a different order each time.
