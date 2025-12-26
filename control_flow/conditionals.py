print("CONDITIONALS")
print("-" * 70)

# Example variables
age = 18
is_student = True

# Conditional statements
if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You are just an adult!")
else:
    print("You are an adult.")

# Nested conditionals
if is_student:
    if age < 25:
        print("You are a young student.")
    else:
        print("You are a mature student.")
else:
    print("You are not a student.")

# Using logical operators
if age >= 18 and is_student:
    print("You are an adult student.")
if age < 18 or not is_student:
    print("You are either a minor or not a student.")

# Ternary conditional operator
status = "minor" if age < 18 else "adult"
print(f"You are classified as a {status}.")

# match case statement (Python 3.10+)
day = "Monday"
match day:
    case "Monday":
        print("Start of the work week.")
    case "Friday":
        print("End of the work week.")
    case "Saturday" | "Sunday":
        print("It's the weekend!")
    case _:
        print("It's a regular weekday.")

mark = 85
# Grading using match case
match mark:
    case m if m >= 90:
        print("Grade: A")
    case m if m >= 80:
        print("Grade: B")
    case m if m >= 70:
        print("Grade: C")
    case m if m >= 60:
        print("Grade: D")
    case _:
        print("Grade: F")
# ============================================================================
