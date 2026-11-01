import argparse
import argparse
import json
import os
import sys
import sys


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


def main(argv=None):
    parser = argparse.ArgumentParser(prog="todos.py")
    parser.add_argument("--file", default="todos.json", help="store path (default: todos.json)")
    sub = parser.add_subparsers(dest="command", required=True)
    add = sub.add_parser("add", help="add a todo")
    add.add_argument("text")
    sub.add_parser("list", help="list todos")
    args = parser.parse_args(argv)

    if args.command == "add":
        try:
            todo = add_todo(args.file, args.text)
        except ValueError as e:
            print(f"error: {e}", file=sys.stderr)
            return 1
        print(f"{todo['id']}. [ ] {todo['text']}")
        return 0

    todos = list_todos(args.file)
    if not todos:
        print("No todos.")
    for t in todos:
        print(f"{t['id']}. [{'x' if t['done'] else ' '}] {t['text']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
