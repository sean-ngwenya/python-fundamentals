print("\nOOP - INHERITANCE & POLYMORPHISM")
print("-" * 70)


# Base class
class Animal:
    def speak(self) -> str:  # Abstract method
        raise NotImplementedError("Subclasses must implement this method")


class Dog(Animal):  # Inherits from Animal
    def speak(self) -> str:  # Implements speak method
        return "Woof"


class Cat(Animal):
    def speak(self) -> str:
        return "Meow"


# Function demonstrating polymorphism
def make_animal_speak(animal: Animal) -> None:  # Accepts any Animal subclass
    print(animal.speak())


# Example usage
if __name__ == "__main__":
    animals = [Dog(), Cat()]  # List of Animal objects

    for animal in animals:
        make_animal_speak(animal)  # Polymorphic behavior
