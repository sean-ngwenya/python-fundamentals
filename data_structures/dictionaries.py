print("\n DATA STRUCTURES: DICTIONARIES")
print("-" * 70)

# Creating a dictionary
student = {
    "name": "John Doe",
    "age": 20,
    "courses": ["Python", "AI", "Statistics"],
    "gpa": 3.8,
}

# Accessing Dictionary items
print(f"Student: {student}")
print(f"Name: {student['name']}")
print(f"Courses: {student['courses']}")

# Add new key
student["university"] = "Your University"
print(f"After adding university: {student}")

# Dictionary methods
print(f"Keys: {student.keys()}")
print(f"Values: {student.values()}")
print(
    f"Sex: {student.get('sex', 'Not specified')}"
)  # Using get() to avoid KeyError & set default value
