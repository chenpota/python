from flask import Blueprint

teacher = Blueprint('teacher', __name__)


@teacher.route('/teacher')
def show():
    return 'teacher', 200
