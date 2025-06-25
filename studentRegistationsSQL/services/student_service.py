import dao.student_dao as dao
from models.student import Student


def create_record(name, email, age):
    student = Student(name, email, age)
    if age >= 130:
        print ('erro idade iconpleta')
        return
    if age < 18:
        print (f'sua idade é {age} aceitamos matriculas  apenas para maior de 18 anos, tente novamente mais tarde :(')
        return
    
    dao.insert_student(student)

def display_record():
    return dao.get_all_students()
