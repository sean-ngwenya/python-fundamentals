# Creating an Individual Class Object
print("\nOOP: CLASS OBJECTS")
print("-" * 70)


# Simple class definition
class Person:
    """Represents a simple person entity."""

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"Hello, my name is {self.name} and I am {self.age} years old."


# Example usage
if __name__ == "__main__":
    person = Person("Craig", 19)
    print(person.greet())
