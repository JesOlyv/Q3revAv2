import sqlite3

# Conectar ao banco de dados SQLite
conexao = sqlite3.connect('carros.db')

# Criar cursor para executar comandos SQL
cursor = conexao.cursor()

# Criar a tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cars (
        ID_CAR INTEGER PRIMARY KEY,
        CAR TEXT,
        TEXT_SPECS TEXT,
        TYRE TEXT,
        HP INTEGER,
        COLOR TEXT,
        PRICE REAL
    )
''')

# Inserir dados na tabela
car_data = ('1', 'Carro 1', 'Especificações do Carro 1', 'Pneu 1', 200, 'Vermelho', 10000.0)
cursor.execute('INSERT OR IGNORE INTO cars (ID_CAR, CAR, TEXT_SPECS, TYRE, HP, COLOR, PRICE) VALUES (?, ?, ?, ?, ?, ?, ?)', car_data)

car_data = ('2', 'Carro 2', 'Especificações do Carro 2', 'Pneu 2', 180, 'Azul', 15000.0)
cursor.execute('INSERT OR IGNORE INTO cars (ID_CAR, CAR, TEXT_SPECS, TYRE, HP, COLOR, PRICE) VALUES (?, ?, ?, ?, ?, ?, ?)', car_data)

# Salvar as alterações no banco de dados
conexao.commit()

# Recuperar e exibir os dados da tabela
cursor.execute('SELECT * FROM cars')
dados = cursor.fetchall()

for registro in dados:
    print(registro)

# Fechar a conexão com o banco de dados
conexao.close()
