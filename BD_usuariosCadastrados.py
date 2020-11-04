import sqlite3
import os.path

caminho = "Bancos de dados/usuariosCadastrados.db"
# Verifica se o arquivo usuariosCadastrados existe
existe = os.path.exists(caminho)

# Cria o arquivo
connection = sqlite3.connect(caminho)

# navega pelo arquivo
c = connection.cursor()

# id INTEGER PRIMARY KEY AUTOINCREMENT
def criar_tabela():
    c.execute(
        """CREATE TABLE IF NOT EXISTS dados (
            nome text,
            senha text,
            UNIQUE(nome)
            )""")


def entradaDados(nome, senha):
    if existe == False:
        criar_tabela()
        c.execute(
            "INSERT OR IGNORE INTO dados (nome, senha) VALUES ('admin', 'admin')")
        c.execute("INSERT OR IGNORE INTO dados (nome, senha) VALUES ('adm', 'adm')")
    else:
        c.execute(
            "INSERT OR REPLACE INTO dados (nome, senha) VALUES ('"+nome+"','"+senha+"')")
    connection.commit()


sql = 'SELECT * FROM dados WHERE nome=? and senha=?'
def leDados(nome,senha):
    for linha in c.execute(sql, (nome,senha,)):
        if linha == "":
            return False
        else:
            return True

def fechaConexao():
    c.close()
    connection.close()
