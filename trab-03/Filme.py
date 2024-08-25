class Filme:
    def __init__(self, titulo, ano, genero):
        self.titulo = titulo
        self.ano = ano
        self.genero = genero
        self.disponibilidade = True  # Inicialmente, todos os filmes estão disponíveis

    def __str__(self):
        return f"{self.titulo} ({self.ano}) - {self.genero} - {'Disponível' if self.disponibilidade else 'Indisponível'}"
