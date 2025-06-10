import sqlite3
from contextlib import contextmanager
DB_NAME = " C:\Users\Fraiburgo\Desktop\LAB\studentRegistationsSQL\models\student.py"
@contextmanager


def get_cursor():
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()

    try:
        yield cursor
        conexao.commit()

    except sqlite3.IntegrityError as e:
        conexao.rollback()
        print(f"Ocorreu o erro de integridade no banco de dados{e}")

    except sqlite3.ProgrammingError as e:
        conexao.rollback()
        print (f"Ocorreu um erro de programcao {e}")
    except sqlite3.OperationalError as e:
        conexao.rollback()
        print(f"ocorreu um erro do 5 operacional: {e}")
    except sqlite3.DatabaseError as e:
        conexao.rollback()
        print(f"erro de banco de dados{e}")
        
    except Exception as e:
        conexao.rollback()
        print(f"Erro inesperado:{e}")
        raise
    finally:
        conexao.close()

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