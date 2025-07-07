import sqlite3


class DBProxy:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.connection.execute("""
        CREATE TABLE IF NOT EXISTS score (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        score INTEGER NOT NULL,
        date TEXT NOT NULL)
        """)

    def save(self, score_dict: dict):
        self.connection.execute('INSERT INTO score (nome, score, date) VALUES (:name, :score, :date)', score_dict)
        self.connection.commit() # Comando para inserir o comando de cima

    def top10(self) -> list: # Metodo que irá fazer aparecer toda a lista em ordem de no max 10
        return self.connection.execute('SELECT * FROM score ORDER BY score DESC LIMIT 10').fetchall()

    def close(self): # Boa pratica para encerrar e não gerar possiveis erros no banco de dados
        return self.connection.close()

