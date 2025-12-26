import json
from pathlib import Path

DATA_FILE = Path("todos.json")


# Load existing todos or return empty list
def load_todos() -> list[str]:
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text())
    return []


# Save todos to file
def save_todos(todos: list[str]) -> None:
    DATA_FILE.write_text(json.dumps(todos, indent=2))


# Add a new todo
def add_todo(task: str) -> None:
    todos = load_todos()
    todos.append(task)
    save_todos(todos)


# List all todos
def list_todos() -> None:
    todos = load_todos()
    for index, task in enumerate(todos, start=1):
        print(f"{index}. {task}")


# CLI loop
if __name__ == "__main__":
    while True:
        command = input("Enter command (add/list/exit): ").strip().lower()

        if command == "add":
            task = input("Enter task: ")
            add_todo(task)
        elif command == "list":
            list_todos()
        elif command == "exit":
            break
        else:
            print("Unknown command")
