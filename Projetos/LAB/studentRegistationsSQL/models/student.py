#essa classe/objeto aluno é OO Orientado a objetos
class Student:
    
    
    #metodo construtor da classe aluno/student
    def __init__(self, name, email, age, id =None):
        self.id = id
        self.name = name
        self.email = email
        self.age = age
        


    def __repr__(self):
        return f"student(id={self.id}), Name = {self.name}, Email={self.email}, age{self.age}"