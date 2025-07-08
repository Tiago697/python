import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import services.student_service as service
from models.student import Student

PROJECT_DIR = "C:\\Users\\Fraiburgo\\Desktop\\LAB\\studentRegistationsSQL\\"

def mainMenu():
    print("\n===== MENU =====")
    print("1. Cadastrar Aluno")
    print("2. Listar Alunos")
    print("3. Atualizar Aluno")
    print("4. Deletar Aluno")
    print("5. Sair")
    return input("Escolha uma opção: ")

def show_students():
    students = service.display_record()
    for student in students:
        print(f"{student.id} - {student.name} - {student.email} - {student.age}")

if __name__ == "__main__":
    service.create_table()

    while True:
        opcao = mainMenu()

        if opcao == "1":
            name = input("Nome do aluno: ")
            email = input("Email do aluno: ")
            age = int(input("Idade do aluno: "))
            service.create_record(name, email, age)
            show_students()

        elif opcao == "2":
            show_students()

        elif opcao == "3":
            student_id = int(input("ID do aluno a ser atualizado: "))
            name = input("Novo nome: ")
            email = input("Novo email: ")
            age = int(input("Nova idade: "))
            service.update_record(student_id, name, email, age)
            show_students()

        elif opcao == "4":
            student_id = int(input("ID do aluno a ser excluído: "))
            service.delete_record(student_id)
            show_students()

        elif opcao == "5":
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")
