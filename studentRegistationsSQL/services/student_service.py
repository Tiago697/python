import dao.student_dao as dao
from models.student import Student


def create_record(name, email, age):
    student = Student(name, email, age)
    if age >= 130:
        print ('erro idade iconpleta')
        return
    if age < 10:
        print ('aceitamos matriclas apenas apenas para maior de 10 anos')
        return
    
    dao.insert_student(student)