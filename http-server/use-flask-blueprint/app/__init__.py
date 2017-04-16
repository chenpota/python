from flask import Flask
from app.teacher import teacher
from app.student import student


def create_server():
    app = Flask(__name__)
    app.register_blueprint(teacher)
    app.register_blueprint(student)

    return app
