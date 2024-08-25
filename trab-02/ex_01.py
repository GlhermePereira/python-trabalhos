def menu():
	print("Escolha uma opcao:")
	print("1. Adicionar contato")
	print("2. Exibir todos os contatos")
	print("3. Buscar contato pelo nome")
	print("4. Sair")

def adicionar_contato(contatos):
	nome = input("Digite o nome do contato: ")
	telefone = input("Digite o numero de telefone: ")
	contatos[nome] = telefone
	print(f"Contato '{nome}' adicionado com sucesso.")

def exibir_contatos(contatos):
	if contatos:
		print("Contatos cadastrados:")
		for nome,telefone in contatos.items():
			print(f"Nome: {nome}, Telefone: {telefone}")
	else:
		print("Nenhum contato cadastrados.")

def buscar_contato(contatos):
	nome = input("Digite o nome do contato para buscar: ")
	telefone = contatos.get(nome, "Contato nao encontrado.")
	print(f"{nome}:{telefone}")

def main():
	contatos = {}
	while True:
		menu()
		print("\n")
		opcao = input("Digite sua opcao: ")
		if opcao == '1':
			adicionar_contato(contatos)
		elif opcao == '2':
			exibir_contatos(contatos)
		elif opcao == '3':
			buscar_contato(contatos)
		elif opcao == '4':
			print("Saindo do programa...")
			break
		else: 
			print("Opcao invalida. Tente novamente.")

if __name__ == "__main__":
	main()

