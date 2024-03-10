import os
import shutil

def delete_pycache():
    try:
        shutil.rmtree("persona/__pycache__")
        print("O diretório _pycache_ foi deletado com sucesso.")
    except FileNotFoundError:
        print("O diretório _pycache_ não existe.")

def delete_migrations():
    try:
        shutil.rmtree("persona/migrations")
        print("O diretório migrations foi deletado com sucesso.")
    except FileNotFoundError:
        print("O diretório migrations não existe.")

def delete_database():
    try:
        os.remove("db.sqlite3")
        print("O banco de dados foi deletado com sucesso.")
    except FileNotFoundError:
        print("O banco de dados não existe.")

# Chame as funções conforme necessário
delete_pycache()
delete_migrations()
delete_database()