import unittest
from app import create_app, tasks

class TodoAppTestCase(unittest.TestCase):
    def setUp(self):
        # Create an app instance for testing
        self.app = create_app().test_client()
        self.app.testing = True

    def tearDown(self):
        # Clear the tasks list after each test
        tasks.clear()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'To-Do List', response.data)

    def test_add_task(self):
        response = self.app.post('/add', data={'task': 'Test Task'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Task', response.data)

    def test_delete_task(self):
        # First, add a task
        self.app.post('/add', data={'task': 'Task to Delete'}, follow_redirects=True)
        
        # Then, delete the task
        response = self.app.get('/delete/0', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Task to Delete', response.data)

if __name__ == '__main__':
    unittest.main()
