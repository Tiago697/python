import sys
import os
PROJECT_DIR = "C:\\Users\\Fraiburgo\\Desktop\\LAB\\studentRegistationsSQL\\"
sys.path.append(os.path.abspath(PROJECT_DIR))



# ... código anterior mantido ...

def show_students():
    students = service.display_record()
    for student in students:
        print(f"{student.id} - {student.name} - {student.email} - {student.age}")

if __name__ == "__main__":
    createTable()

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
            break

        else:
            print("Opção inválida. Tente novamente.")
