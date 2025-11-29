# todos/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Todo

class TodoModelTest(TestCase):
    """Test the database structure and defaults."""
    
    def test_todo_creation_defaults(self):
        # Scenario: Create a simple todo without specifying 'is_resolved'
        todo = Todo.objects.create(title="Buy Milk")
        
        # Check: Did it save?
        self.assertEqual(todo.title, "Buy Milk")
        # Check: Is it unresolved by default? (Crucial logic check)
        self.assertFalse(todo.is_resolved)
        # Check: Does the string representation work? (Important for Admin panel)
        self.assertEqual(str(todo), "Buy Milk")


class TodoViewTest(TestCase):
    """Test the pages and user interactions."""

    def setUp(self):
        # Create a sample task to use in tests below
        self.todo = Todo.objects.create(title="Test Task")

    def test_list_view_loads(self):
        # Scenario: User visits the homepage
        response = self.client.get(reverse('todo-list'))
        
        # Check: Page loads successfully (200 OK)
        self.assertEqual(response.status_code, 200)
        # Check: Our task is actually visible in the HTML
        self.assertContains(response, "Test Task")

    def test_create_new_todo(self):
        # Scenario: User submits the "New Task" form
        response = self.client.post(reverse('todo-create'), {
            'title': 'Walk the dog',
            'description': 'Go to the park',
            'due_date': '2025-12-31'
        })
        
        # Check: Redirects back to list after success (302 Found)
        self.assertEqual(response.status_code, 302)
        # Check: Is it in the database now?
        self.assertEqual(Todo.objects.count(), 2) # 1 from setUp + 1 new one

    def test_toggle_status_logic(self):
        # Scenario: User clicks the "Check/Uncheck" button
        # 1. Verify it starts False
        self.assertFalse(self.todo.is_resolved)
        
        # 2. Hit the toggle URL
        url = reverse('todo-toggle', args=[self.todo.id])
        self.client.get(url)
        
        # 3. Reload from DB and check if it flipped to True
        self.todo.refresh_from_db()
        self.assertTrue(self.todo.is_resolved)
        
        # 4. Hit it again to check if it toggles back to False
        self.client.get(url)
        self.todo.refresh_from_db()
        self.assertFalse(self.todo.is_resolved)