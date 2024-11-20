from pymongo import MongoClient

# Função para conectar ao banco de dados
def get_database():
    client = MongoClient("mongodb://localhost:27017/")  # Conexão local
    return client["biblioteca"]  # Retorna o banco de dados 'biblioteca'
