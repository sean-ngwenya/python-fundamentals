# Tuples in Python
print("\nDATA STRUCTURES: TUPLES")
print("-" * 70)

# Creating tuples
coordinates = (10.0, 20.0)
person = ("Alice", 30, "Engineer")

# Accessing tuple elements
x_coord = coordinates[0]
name = person[0]

print(f"X Coordinate: {x_coord}")
print(f"Name: {name}")

tuple_length = len(person)
print(f"Length of person tuple: {tuple_length}")


# Tuples are immutable
# The following line would raise an error if uncommented
# coordinates[0] = 15.0
