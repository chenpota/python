import unittest
from flask import current_app
from flask import url_for
from app import create_server


class TestApp(unittest.TestCase):

    def setUp(self):
        self.server = create_server()
        self.server_ctx = self.server.app_context()
        self.server_ctx.push()
        self.client = self.server.test_client()

    def tearDown(self):
        self.server_ctx.pop()

    def test_teacher(self):
        rsp = self.client.get('teacher')
        self.assertEqual(rsp.data.decode('utf-8'), 'teacher')
        self.assertEqual(rsp.status_code, 200)

    def test_student(self):
        rsp = self.client.get('student')
        self.assertEqual(rsp.data.decode('utf-8'), 'student')
        self.assertEqual(rsp.status_code, 200)

    def test_strenger(self):
        rsp = self.client.get('strenger')
        self.assertEqual(rsp.status_code, 404)
