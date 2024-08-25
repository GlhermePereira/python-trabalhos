class Locadora:
    def __init__(self):
        self.filmes = []
        self.clientes = []
        self.filmes_alugados = {}

    def adicionar_filme(self, filme):
        self.filmes.append(filme)

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def alugar_filme(self, titulo, id_cliente):
        filme = next((f for f in self.filmes if f.titulo == titulo), None)
        cliente = next((c for c in self.clientes if c.id_cliente == id_cliente), None)

        if filme and cliente:
            if filme.disponibilidade:
                filme.disponibilidade = False
                self.filmes_alugados[titulo] = cliente
                print(f"Filme '{titulo}' alugado para {cliente.nome}.")
            else:
                print(f"Filme '{titulo}' não está disponível.")
        else:
            if not filme:
                print(f"Filme '{titulo}' não encontrado.")
            if not cliente:
                print(f"Cliente com ID '{id_cliente}' não encontrado.")

    def listar_filmes_disponiveis(self):
        for filme in self.filmes:
            if filme.disponibilidade:
                print(filme)

    def listar_filmes_alugados(self):
        for titulo, cliente in self.filmes_alugados.items():
            print(f"{titulo} - Alugado por {cliente.nome}")

    def listar_clientes(self):
        for cliente in self.clientes:
            print(cliente)
