#!/usr/bin/env python3

import os
from os.path import isfile
from os.path import getsize
import sqlite3

MAX_RECORD_SIZE = 9


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
                name    TEXT CHECK(name NOT NULL AND LENGTH(name) <= 20)
            );

            CREATE TABLE scores(
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id  INTEGER NOT NULL,
                class       TEXT CHECK(class NOT NULL AND LENGTH(class) <= 20),
                score       INTEGER NOT NULL,

                FOREIGN KEY (student_id) REFERENCES students(id)
            );

            CREATE UNIQUE INDEX index_students_id_class ON scores(student_id, class);
        ''')

        db.commit()


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


def query_all(file):
    with sqlite3.connect(file) as db:
        cur = db.cursor()

        cur_students = cur.execute(
            "SELECT id, name FROM students ORDER BY id ASC")

        for id_, name_ in cur_students.fetchall():
            print('\t', id_, name_)

            cur_scores = cur.execute(
                "SELECT id, student_id, class, score FROM scores WHERE student_id=? ORDER BY id ASC",
                (id_,))

            for id_, student_id_, class_, score_ in cur_scores.fetchall():
                print('\t\t', id_, student_id_, class_, score_)


def query_student(file, student):
    with sqlite3.connect(file) as db:
        cur = db.cursor()

        cur_student = cur.execute(
            "SELECT id, name FROM students WHERE name=? ORDER BY id ASC",
            (student,))

        row_student = cur_student.fetchone()

        cur_scores = cur.execute(
            """
            SELECT id, student_id, class, score
            FROM scores
            WHERE student_id=?
            ORDER BY id ASC
            """,
            (row_student[0],))

        print('\t', row_student[0], row_student[1])

        for id_, student_id_, class_, score_ in cur_scores.fetchall():
            print('\t\t', id_, student_id_, class_, score_)


def query_student_with_index_size(file, student, next_record_index=0, record_size=MAX_RECORD_SIZE):
    if next_record_index < 0:
        next_record_index = 0

    if record_size < 0 or record_size > 99:
        record_size = MAX_RECORD_SIZE

    with sqlite3.connect(file) as db:
        cur = db.cursor()

        cur_scores = cur.execute(
            """
            SELECT id, student_id, class, score
            FROM scores
            WHERE
                id>=? AND
                student_id = (SELECT id FROM students WHERE name = ?)
            ORDER BY id ASC
            """,
            (next_record_index, student))

        row_scores = cur_scores.fetchmany(record_size)

        cur_id = 0

        for cur_id, student_id_, class_, score_ in row_scores:
            print('\t\t', cur_id, student_id_, class_, score_)

        return cur_id + 1 if cur_id != 0 else 0


def main():
    file = './db'

    create_db(file)
    is_sqlite3_file(file)

    # Insert two students
    print('Insert two students:')
    students = (
        (
            'Michael',
            (
                ('Chinese', 80),
                ('Math', 20)
            )
        ),
        (
            'Jack',
            (
                ('English', 40),
                ('Music', 75),
                ('Physical', 5),
                ('Chemistry', 12)
            )
        )
    )

    for student in students:
        insert(file, student)

    # Insert a student with duplicated scores
    print('Insert a student with duplicated scores:')
    students = (
        (
            'Daniel',
            (
                ('Chinese', 80),
                ('Chinese', 20)
            )
        ),
    )

    try:
        for student in students:
            insert(file, student)
    except sqlite3.IntegrityError as ex:
        print('\t', ex)

    # Query all
    print('Query all:')
    query_all(file)

    # Query a student's info
    print("Query a student's info:")
    query_student(file, 'Jack')

    # Query a student's score by index and size
    print('Query student:')
    next_record_index = 0
    record_size = 3
    times = 1

    while True:
        print('\tsearch times:', times)

        next_record_index = query_student_with_index_size(
            file,
            'Jack',
            next_record_index,
            record_size)

        if next_record_index == 0:
            break

        times += 1

if __name__ == '__main__':
    main()
