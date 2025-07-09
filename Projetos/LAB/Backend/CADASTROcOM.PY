import sqlite3

# Função para exibir o menu principal
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

# Função para cadastrar aluno
def cadastrar_aluno(nome, email, idade):
    conexao = sqlite3.connect("escola.db")
    cursor = conexao.cursor()
    try:
        cursor.execute("INSERT INTO aluno (nome, email, idade) VALUES (?, ?, ?)",
                       (nome, email, idade))
        conexao.commit()
        print("✅ Aluno cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print("❌ Erro: email já cadastrado.")
    finally:
        conexao.close()

# Função para listar todos os alunos
def listar_alunos():
    conexao = sqlite3.connect("escola.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM aluno")
    alunos = cursor.fetchall()
    conexao.close()

    if alunos:
        print("\nLista de Alunos:")
        for aluno in alunos:
            print(f"ID: {aluno[0]}, Nome: {aluno[1]}, Email: {aluno[2]}, Idade: {aluno[3]}")
    else:
        print("Nenhum aluno cadastrado.")

# Função para atualizar aluno
def atualizar_aluno(id, nome, email, idade):
    conexao = sqlite3.connect("escola.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM aluno WHERE id = ?", (id,))
    if cursor.fetchone():
        try:
            cursor.execute("UPDATE aluno SET nome = ?, email = ?, idade = ? WHERE id = ?",
                           (nome, email, idade, id))
            conexao.commit()
            print("✅ Aluno atualizado com sucesso!")
        except sqlite3.IntegrityError:
            print("❌ Erro: email já cadastrado.")
    else:
        print("❌ Aluno com esse ID não encontrado.")
    conexao.close()

# Função para excluir aluno
def excluir_aluno(id):
    conexao = sqlite3.connect("escola.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM aluno WHERE id = ?", (id,))
    if cursor.fetchone():
        cursor.execute("DELETE FROM aluno WHERE id = ?", (id,))
        conexao.commit()
        print("✅ Aluno excluído com sucesso!")
    else:
        print("❌ Aluno com esse ID não encontrado.")
    conexao.close()

# Execução principal
if __name__ == "__main__":
    conectar()
    
    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            nome = input("Nome: ").strip()
            email = input("Email: ").strip()
            try:
                idade = int(input("Idade: ").strip())
                cadastrar_aluno(nome, email, idade)
            except ValueError:
                print("❌ Idade inválida. Deve ser um número inteiro.")

        elif opcao == "2":
            listar_alunos()

        elif opcao == "3":
            try:
                id = int(input("ID do aluno a ser atualizado: ").strip())
                nome = input("Novo Nome: ").strip()
                email = input("Novo Email: ").strip()
                idade = int(input("Nova Idade: ").strip())
                atualizar_aluno(id, nome, email, idade)
            except ValueError:
                print("❌ Entrada inválida. Use números para ID e idade.")

        elif opcao == "4":
            try:
                id = int(input("ID do aluno a ser excluído: ").strip())
                excluir_aluno(id)
            except ValueError:
                print("❌ ID inválido.")

        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")
