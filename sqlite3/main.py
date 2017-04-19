#!/usr/bin/env python3

import os
from os.path import isfile
from os.path import getsize
import sqlite3


def is_sqlite3_file(file):
    '''
    Refer to http://www.sqlite.org/fileformat.html#database_header
    '''

    if not isfile(file) or getsize(file) < 100:
        return False

    with open(file, 'rb') as fd:
        return fd.read(16) == b'SQLite format 3\x00'


def create_db(file):
    try:
        os.remove(file)
    except:
        pass

    with sqlite3.connect(file) as db:
        cur = db.cursor()

        cur.executescript('''
            CREATE TABLE students(
                id      INTEGER PRIMARY KEY AUTOINCREMENT,
                name    TEXT CHECK(name IS NOT NULL AND LENGTH(name) <= 3)
            );

            CREATE TABLE scores(
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id  INTEGER NOT NULL,
                class       TEXT CHECK(class IS NOT NULL AND LENGTH(class) <= 10),
                score       INTEGER NOT NULL,

                FOREIGN KEY (student_id) REFERENCES students(id)
            );

            CREATE UNIQUE INDEX index_students_id_class ON scores(student_id, class);
        ''')

        db.commit()

'''
def insert_db(file):
    students = [('王小明',), ('葉大雄',)]

    with sqlite3.connect(file) as db:
        cur = db.cursor()

        cur.executemany("INSERT INTO students('name') VALUES (?)", students)

        db.commit()
'''


def insert_student(db, student):
    cur = db.cursor()

    cur.execute("INSERT INTO students (name) VALUES (?)", (student,))

    return cur.lastrowid


def insert_scores(db, student_id, scores):
    datas = []

    for score in scores:
        data = [student_id]
        data.extend(score)
        datas.append(tuple(data))

    cur = db.cursor()

    cur.executemany(
        "INSERT INTO scores(student_id, class, score) VALUES (?, ?, ?)",
        datas)


def insert(file, infos):
    with sqlite3.connect(file) as db:
        student_id = insert_student(db, infos[0])
        insert_scores(db, student_id, infos[1])

        db.commit()


def main():
    file = './db'

    if not is_sqlite3_file(file):
        create_db(file)

    students = (
        (
            '王小明',
            (
                ('國文', 80),
                ('數學', 20)
            )
        ),
        (
            '葉大雄',
            (
                ('英文', 40),
                ('物理', 75)
            )
        )
    )

    for student in students:
        insert(file, student)

if __name__ == '__main__':
    main()
