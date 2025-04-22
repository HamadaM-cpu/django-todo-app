from django.test import TestCase
from .models import Todo

class TodoModelTest(TestCase):

    def test_todo_creation(self):
        todo = Todo.objects.create(
            title="Test Todo",
            description="This is a test todo item.",
            deadline="2025-12-31",
            completed=False
        )
        self.assertEqual(todo.title, "Test Todo")
        self.assertFalse(todo.completed)