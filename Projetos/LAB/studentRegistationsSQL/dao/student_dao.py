from db.connection import get_cursor
from models.student import Student

def insert_student(student):
    with get_cursor() as cursor:
        cursor.execute(
            "INSERT INTO aluno (nome, email, idade) VALUES (?, ?, ?)",
            (student.name, student.email, student.age)
        )

def get_all_students():
    with get_cursor() as cursor:
        cursor.execute("SELECT * FROM aluno")
        rows = cursor.fetchall()
        return [Student(id=row[0], name=row[1], email=row[2], age=row[3]) for row in rows]

def update_student(student_id, name, email, age):
    with get_cursor() as cursor:
        cursor.execute(
            "UPDATE aluno SET nome = ?, email = ?, idade = ? WHERE id = ?",
            (name, email, age, student_id)
        )

def delete_student(student_id):
    with get_cursor() as cursor:
        cursor.execute("DELETE FROM aluno WHERE id = ?", (student_id,))

def create_table():
    with get_cursor() as cursor:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS aluno (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                idade INTEGER NOT NULL
            )
        ''')
