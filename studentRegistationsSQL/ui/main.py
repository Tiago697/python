import sys
import os
PROJECT_DIR = "C:\\Users\\Fraiburgo\\Desktop\\LAB\\studentRegistationsSQL\\"
sys.path.append(os.path.abspath(PROJECT_DIR))



from db.connection import createTable
import services.student_service as service


def show_students():
    students = service.display_record()
    for student in students:
        print (f"{student.id} - {student.name} - {student.email} - {student.age}")



def mainMenu() -> str:
    print("\nSistema de Cadastro de Alunos")
    print("1. Cadastrar Aluno")
    print("2. Listar Alunos")
    print("3. Atualizar Aluno")
    print("4. Excluir Aluno")
    print("5. Sair")
    opcao:str = input("escolha uma opcao")
    return opcao


if __name__ == "__main__":
    createTable()
    
    while True:
        mainMenu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            name = input("Nome do aluno: ")
            email = input("Email do aluno: ")
            age = int(input("Idade do aluno: "))
            service.create_record(name, email, age)
            show_students()
        
        
        elif opcao == "2":
            show_students()

            


            
        if opcao == "5":
            break


