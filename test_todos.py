import os
import tempfile
import unittest

from todos import add_todo, list_todos


class StoreTests(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.path = os.path.join(self.dir.name, "todos.json")

    def tearDown(self):
        self.dir.cleanup()

    def test_missing_file_is_empty(self):
        self.assertEqual(list_todos(self.path), [])

    def test_add_and_list(self):
        todo = add_todo(self.path, "buy milk")
        self.assertEqual(todo, {"id": 1, "text": "buy milk", "done": False})
        self.assertEqual(list_todos(self.path), [todo])

    def test_id_increments(self):
        add_todo(self.path, "a")
        add_todo(self.path, "b")
        self.assertEqual([t["id"] for t in list_todos(self.path)], [1, 2])

    def test_empty_text_rejected(self):
        for bad in ("", "   ", None):
            with self.assertRaises(ValueError):
                add_todo(self.path, bad)
        self.assertEqual(list_todos(self.path), [])


if __name__ == "__main__":
    unittest.main()
