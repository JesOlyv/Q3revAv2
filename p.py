import psycopg2

# Conectar ao banco de dados PostgreSQL
conexao = psycopg2.connect(
    host="localhost",
    database="nomedobanco",
    user="seuusuario",
    password="suasenha"
)

# Criar cursor para executar comandos SQL
cursor = conexao.cursor()

# Criar a tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cars (
        ID_CAR SERIAL PRIMARY KEY,
        CAR TEXT,
        TEXT_SPECS TEXT,
        TYRE TEXT,
        HP INTEGER,
        COLOR TEXT,
        PRICE REAL
    )
''')

# Inserir dados na tabela
car_data = ('Carro 1', 'Especificações do Carro 1', 'Pneu 1', 200, 'Vermelho', 10000.0)
cursor.execute('INSERT INTO cars (CAR, TEXT_SPECS, TYRE, HP, COLOR, PRICE) VALUES (%s, %s, %s, %s, %s, %s)', car_data)

car_data = ('Carro 2', 'Especificações do Carro 2', 'Pneu 2', 180, 'Azul', 15000.0)
cursor.execute('INSERT INTO cars (CAR, TEXT_SPECS, TYRE, HP, COLOR, PRICE) VALUES (%s, %s, %s, %s, %s, %s)', car_data)

# Salvar as alterações no banco de dados
conexao.commit()

# Recuperar e exibir os dados da tabela
cursor.execute('SELECT * FROM cars')
dados = cursor.fetchall()

for registro in dados:
    print(registro)

# Fechar a conexão com o banco de dados
conexao.close()
