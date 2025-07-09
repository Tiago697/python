import sqlite3

def mainMenu() -> str:
    print("\nSistema de Cadastro de Alunos")
    print("1. Cadastrar Aluno")
    print("2. Listar Alunos")
    print("3. Atualizar Aluno")
    print("4. Excluir Aluno")
    print("5. Sair")

def createTable():
    conexao = sqlite3.connect("escola.db")  
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS aluno (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            idade INTEGER
        )
    """)
    conexao.commit()
    conexao.close()

# Função para cadastrar aluno no banco de dados
def register(nome: str, email: str, idade: int):
    conexao = sqlite3.connect("escola.db")
    cursor = conexao.cursor()
    try:
        cursor.execute("INSERT INTO aluno (nome, email, idade) VALUES (?, ?, ?)",
                       (nome, email, idade))
        conexao.commit()
        print("Aluno cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: E-mail já cadastrado.")
    finally:
        conexao.close()

def display():
    conexao = sqlite3.connect("escola.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM aluno")
    alunos = cursor.fetchall()
    conexao.close()

    if alunos:
        print("\nLista de alunos cadastrados:")
        for aluno in alunos:
            print(aluno)
    else:
        print("\nNenhum aluno cadastrado.")

def update(id, newName, newEmail, newIdade):


    conexao = sqlite3.connect("escola.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM aluno WHERE id = ?", (id,))
    if cursor.fetchone() is None:
        print("Aluno com esse ID não encontrado.")
    else:
        try:
            cursor.execute("UPDATE aluno SET nome = ?, email = ?, idade = ? WHERE id = ?",
                           (newName, newEmail, newIdade, id))
            conexao.commit()
            print("Aluno atualizado com sucesso!")
        except sqlite3.IntegrityError:
            print("Erro: E-mail já cadastrado para outro aluno.")
    conexao.close()


def delete(id):
    conexao = sqlite3.connect("escola.db")
    cursor = conexao.cursor()

    
    cursor.execute("DELETE FROM aluno WHERE id = ?", 
                   (id,))
    conexao.commit()

        
    print(f"Aluno com ID {id} foi excluído com sucesso.")
    
    
    conexao.close()
    conexao.commit()
    

# Bloco principal de execução
if __name__ == "__main__":
    createTable()
    while True:
        mainMenu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do aluno: ")
            email = input("Email do aluno: ")
            try:
                idade = int(input("Idade do aluno: "))
                register(nome, email, idade)
            except ValueError:
                print("Erro: Idade deve ser um número inteiro.")

        elif opcao == "2":
            display()

        elif opcao == "3":
            try:
                id = int(input("Informe o ID do aluno a ser atualizado: "))
                newName = input("Novo nome: ")
                newEmail = input("Novo email: ")
                newIdade = int(input("Nova idade: "))
                update(id, newName, newEmail, newIdade)
            except ValueError:
                print("Erro: ID e idade devem ser números.")
        elif opcao == "4":
                id = int(input("Informe o ID do aluno a ser excluido: "))
                delete(id)
        elif opcao == "5":
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida ou função ainda não implementada.")
