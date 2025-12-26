print("\nFILE HANDLING - READ & WRITE FILES")
print("-" * 70)


FILE_NAME = "example.txt"


# to write to file
def write_file(text: str) -> None:
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        file.write(text)


# function to read file
def read_file() -> str:
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        return file.read()


# Example usage
if __name__ == "__main__":
    write_file("Hello, this is file handling in Python.")
    content = read_file()
    print(content)
