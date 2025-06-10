from db.connection import get_cursor
from models.student import Student

def insert_student(student):
    with get_cursor() as cursor:
        cursor.execute ("INSERT INTO aluno (nome, email, idade) VALUES (?, ?, ?)",
                       (student.name,student.email,student.age)
                       )