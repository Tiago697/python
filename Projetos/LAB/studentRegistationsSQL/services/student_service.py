import dao.student_dao as dao
from models.student import Student

def create_record(name, email, age):
    student = Student(name, email, age)
    if age >= 130:
        print('Erro: idade incorreta')
        return
    if age < 18:
        print(f'Sua idade é {age}. Aceitamos matrículas apenas para maiores de 18 anos.')
        return
    dao.insert_student(student)

def display_record():
    return dao.get_all_students()

def update_record(student_id, name, email, age):
    if age >= 130 or age < 18:
        print('Erro: idade inválida para atualização.')
        return
    dao.update_student(student_id, name, email, age)

def delete_record(student_id):
    dao.delete_student(student_id)

def create_table():
    dao.create_table()
            