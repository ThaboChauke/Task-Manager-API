import unittest
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
        self.assertEqual(response.status_code, 201)
        self.assertIn('Task created', str(response.data))


if __name__ == '__main__':
    unittest.main()
