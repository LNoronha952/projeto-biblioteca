from models.livros import (
    inserir_livro, listar_por_autor, buscar_por_isbn,
    atualizar_livro, deletar_livro, listar_por_genero,
    listar_mais_paginas, listar_menos_paginas
)

# Testando as funções
if __name__ == "__main__":
    # Exemplo de livro
    livro = {
        "titulo": "Dom Quixote",
        "autor": "Miguel de Cervantes",
        "ano_publicacao": 1605,
        "genero": "Ficção",
        "num_paginas": 863,
        "sinopse": "A história de um cavaleiro que luta contra moinhos de vento.",
        "isbn": "978-3-16-148410-0"
    }

    # Inserir livro
    print("Inserindo livro...")
    inserir_livro(livro)

    # Listar livros de um autor
    print("\nLivros por autor:")
    print(listar_por_autor("Miguel de Cervantes"))

    # Buscar livro pelo ISBN
    print("\nLivro por ISBN:")
    print(buscar_por_isbn("978-3-16-148410-0"))

    # Atualizar livro
    print("\nAtualizando livro...")
    atualizar_livro("978-3-16-148410-0", {"num_paginas": 900})
    print(buscar_por_isbn("978-3-16-148410-0"))

    # Deletar livro
    print("\nDeletando livro...")
    deletar_livro("978-3-16-148410-0")
    print(buscar_por_isbn("978-3-16-148410-0"))
