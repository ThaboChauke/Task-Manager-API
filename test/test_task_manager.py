import unittest
from statistics import pstdev
from token import EQUAL

from main import app, db, Users
from flask_jwt_extended import create_access_token


class TaskManagerAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()
            self.test_user = Users(username='test_user', email='test@example.com', name='Test User')
            self.test_user.set_password('testpassword')
            db.session.add(self.test_user)
            db.session.commit()

            self.token = create_access_token(identity=self.test_user.id)

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_task(self):
        response = self.client.post('/tasks',
                                    json={'title': 'New Task', 'description': 'Task description',
                                          'due_date': '2024-11-10 18:00'},
                                    headers={'Authorization': f'Bearer {self.token}'})

        self.assertEqual(201, response.status_code)
        self.assertIn('Task created', str(response.data))

    def test_create_task_unauthorized(self):
        invalid_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTczMDgzMDQ4OSwianRpIjoiNzQxNjFjMDQtNzU5Yy00MTc4LWJkYzItMTAxYzU4MmJjN2NiIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNzMwODMwNDg5LCJjc3JmIjoiY2M1NjAzY2EtOTE2NC00ZTNjLWEyOGUtNjRmMzI1ZGM2OTYzIiwiZXhwIjoxNzMwODM0MDg5fQ.o1nZyeY8XrnC77SPQwXy4ogCyIqar-gXMdQ6LChAneM"

        response = self.client.post('/tasks',
                                    json={'title': 'New Task', 'description': 'Task description',
                                          'due_date': '2024-11-10 18:00'},
                                    headers={'Authorization': f'Bearer {invalid_token}'})

        self.assertEqual(401, response.status_code)
        self.assertIn('Token has expired', str(response.data))

    def test_get_tasks(self):
        response = self.client.get('/tasks', headers={'Authorization': f'Bearer {self.token}'})

        self.assertEqual(200, response.status_code)
        self.assertIsInstance(response.json.get('tasks'), list)


    def delete_task(self):
        pass

    def update_task(self):
        pass

    def non_existent_user(self):
        pass

    def register_user(self):
        pass


if __name__ == '__main__':
    unittest.main()
