from Filme import Filme
from Cliente import Cliente
from Locadora import Locadora

def main():
    locadora = Locadora()

    while True:
        print("\nMenu:")
        print("1. Adicionar filme")
        print("2. Adicionar cliente")
        print("3. Alugar filme")
        print("4. Listar filmes disponíveis")
        print("5. Listar filmes alugados")
        print("6. Listar clientes")
        print("7. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            titulo = input("Título do filme: ")
            ano = input("Ano de lançamento: ")
            genero = input("Gênero: ")
            filme = Filme(titulo, ano, genero)
            locadora.adicionar_filme(filme)
            print(f"Filme '{titulo}' adicionado.")

        elif escolha == '2':
            id_cliente = input("ID do cliente: ")
            nome = input("Nome do cliente: ")
            cliente = Cliente(id_cliente, nome)
            locadora.adicionar_cliente(cliente)
            print(f"Cliente '{nome}' adicionado.")

        elif escolha == '3':
            titulo = input("Título do filme para alugar: ")
            id_cliente = input("ID do cliente: ")
            locadora.alugar_filme(titulo, id_cliente)

        elif escolha == '4':
            print("Filmes disponíveis:")
            locadora.listar_filmes_disponiveis()

        elif escolha == '5':
            print("Filmes alugados:")
            locadora.listar_filmes_alugados()

        elif escolha == '6':
            print("Clientes cadastrados:")
            locadora.listar_clientes()

        elif escolha == '7':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
