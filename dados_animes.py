import sqlite3

#1-Conecta no BD e cria tabela se não existir
def conecta_bd():
    conexao = sqlite3.connect('titulo.db')
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS animes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            genero TEXT NOT NULL,
            nota REAL NOT NULL
        )
    ''')
    conexao.commit()
    return conexao

#2-Insere Dados
def insere_dados(nome, genero, nota):
    conexao = conecta_bd()
    cursor = conexao.cursor()
    cursor.execute(
        '''
        INSERT INTO animes(nome, genero,nota)
        VALUES (?, ?, ?)
        ''',(nome, genero, nota)
    )
    conexao.commit()
    conexao.close()

# 3- Lista Dados
def obter_dados():
    conexao = conecta_bd()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM animes")
    dados = cursor.fetchall()
    cursor.close()
    return dados