import os
import sys


# function to show system info
def show_system_info() -> None:
    print("Current working directory:", os.getcwd())
    print("Python executable:", sys.executable)
    print("Command-line arguments:", sys.argv)


if __name__ == "__main__":
    show_system_info()
