import sqlite3

# Menu principal do sistema
def menu():
    print("\nSistema de Cadastro de Alunos")
    print("1. Cadastrar Aluno")
    print("2. Listar Alunos")
    print("3. Atualizar Aluno")
    print("4. Excluir Aluno")
    print("5. Sair")

# Cria o banco de dados e a tabela aluno
def conectar():
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

# Função para cadastrar o aluno no DB
def cadastrar_aluno(nome, email, idade):
    conexao = sqlite3.connect("escola.db")
    cursor = conexao.cursor()

    try:
        cursor.execute("INSERT INTO aluno (nome, email, idade) VALUES (?, ?, ?)",
                       (nome, email, idade))
        conexao.commit()
        print("Aluno cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: email já cadastrado.")
    finally:
        conexao.close()

# Execução principal
if __name__ == "__main__":
    conectar()
    
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            try:
                idade = int(input("Idade: "))
                cadastrar_aluno(nome, email, idade)
            except ValueError:
                print("Idade inválida. Por favor, insira um número inteiro.")
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção ainda não implementada.")
