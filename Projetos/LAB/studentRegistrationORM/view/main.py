import sys
from pathlib import Path

#pega o caminho do arquivo atual no caso mais.py
current_file = Path(__file__)

#define a raiz do projeto
project_root = Path(__file__).parent.parent

#adiciona a raiz do projeto no path do python
sys.path.append(str(project_root))


from db.connection import connect_db, close_db
from services.student_service import StudentService

def show_menu():
    print("\n============ Sistema de cadastro de alunos =================")
    print("1. cadastrar Aluno:")
    print("2. Listar Aluno:")

    print("===============================================================")

def main():
    connect_db()
    
    service = StudentService

    while True:
        show_menu()

        opcao = input("Escolha a opcao")

        if opcao == "1":
            name = input("Informe o nome do aluno:")
            age = int(input("informe a idade:"))
            email = input("Informe o e-mail:")
            #chama a segunda camada (service) e passa os dados
            service.register_student(name,age,email)
            print("Aluno cadastrado com sucesso!:")
        
        elif opcao == "5":
            print ("Saindo do sistema")
            break
        else:
            print("Opcao invalida")
    close_db()

if __name__ == "__main__":
    main()
