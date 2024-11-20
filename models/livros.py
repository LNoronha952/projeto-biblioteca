from db_config import get_database

db = get_database()
livros = db["livros"]

def inserir_livro(dados):
    livros.insert_one(dados)
    print("Livro inserido com sucesso!")

def atualizar_livro(isbn, novos_dados):
    resultado = livros.update_one({"isbn": isbn}, {"$set": novos_dados})
    if resultado.modified_count > 0:
        print("Livro atualizado com sucesso!")
    else:
        print("Nenhum livro encontrado com o ISBN fornecido.")

def deletar_livro(isbn):
    resultado = livros.delete_one({"isbn": isbn})
    if resultado.deleted_count > 0:
        print("Livro deletado com sucesso!")
    else:
        print("Nenhum livro encontrado com o ISBN fornecido.")

def listar_por_autor(autor):
    return list(livros.find({"autor": autor}))

def listar_por_genero(genero):
    return list(livros.find({"genero": genero}))

def listar_por_ano(ano):
    return list(livros.find({"ano_publicacao": ano}))

def listar_mais_paginas():
    return list(livros.find().sort("num_paginas", -1).limit(10))

def listar_menos_paginas():
    return list(livros.find().sort("num_paginas", 1).limit(10))

def buscar_por_isbn(isbn):
    return livros.find_one({"isbn": isbn})
