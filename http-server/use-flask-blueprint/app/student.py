from flask import Blueprint

student = Blueprint('student', __name__)


@student.route('/student')
def show():
    return 'student', 200
