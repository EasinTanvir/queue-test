import json
import os


def list_todos(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def add_todo(path, text):
    if not text or not text.strip():
        raise ValueError("todo text must not be empty")
    todos = list_todos(path)
    todo = {
        "id": max((t["id"] for t in todos), default=0) + 1,
        "text": text.strip(),
        "done": False,
    }
    todos.append(todo)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)
    return todo
