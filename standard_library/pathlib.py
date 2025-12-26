from pathlib import Path


# Demonstration of pathlib module
def pathlib_demo() -> None:
    path = Path("sample_folder")
    path.mkdir(exist_ok=True)

    file_path = path / "example.txt"
    file_path.write_text("Pathlib makes file handling easier.")

    print("File exists:", file_path.exists())
    print("File content:", file_path.read_text())


if __name__ == "__main__":
    pathlib_demo()
