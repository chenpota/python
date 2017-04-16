import unittest
from flask import current_app
from app import create_server


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = create_server()
        self.app_ctx = self.app.app_context()
        self.app_ctx.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_ctx.pop()

    def test_teacher(self):
        rsp = self.client.get('/teacher')
        self.assertEqual(rsp.get_data(as_text=True), 'teacher')
        self.assertEqual(rsp.status_code, 200)

    def test_student(self):
        rsp = self.client.get('/student')
        self.assertEqual(rsp.get_data(as_text=True), 'student')
        self.assertEqual(rsp.status_code, 200)

    def test_strenger(self):
        rsp = self.client.get('strenger')
        self.assertEqual(rsp.status_code, 404)
