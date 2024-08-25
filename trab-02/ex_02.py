import os

# Caminho dos arquivos
arquivo_vendas = os.path.expanduser('~/Documents/web-3/vendas.txt')
arquivo_relatorio = os.path.expanduser('~/Documents/web-3/relatorio.txt')

def processar_vendas(arquivo_vendas):
    vendas_por_produto = {}
    vendas_por_dia = {}
    total_geral = 0     
    with open(arquivo_vendas, 'r') as file:
        for linha in file:
            # Remove espaços extras e ignora linhas em branco
            linha = linha.strip()
            if not linha:
                continue

            # Tenta detectar o delimitador correto
            if ',' in linha:
                elementos = linha.split(',')
            else:
                elementos = linha.split()

            if len(elementos) != 4:
                print(f"Erro: Linha com formato incorreto ignorada: {linha}")
                continue

            data, produto, quantidade, preco_unitario = elementos
            try:
                quantidade = int(quantidade)
                preco_unitario = float(preco_unitario)
            except ValueError:
                print(f"Erro: Valores numéricos inválidos na linha: {linha}")
                continue

            total_venda = quantidade * preco_unitario

            if produto in vendas_por_produto:
                vendas_por_produto[produto] += total_venda
            else:
                vendas_por_produto[produto] = total_venda

            if data in vendas_por_dia:
                vendas_por_dia[data] += total_venda
            else:
                vendas_por_dia[data] = total_venda

    total_geral = sum(vendas_por_produto.values())
    return vendas_por_produto, vendas_por_dia, total_geral

def gerar_relatorio(vendas_por_produto, vendas_por_dia, total_geral, arquivo_relatorio):
    with open(arquivo_relatorio, 'w') as file:
        file.write("Relatório de Vendas\n")
        file.write("===================\n\n")

        file.write("Total de Vendas por Produto:\n")
        for produto, total in vendas_por_produto.items():
            file.write(f"{produto}: R$ {total:.2f}\n")

        file.write("\nTotal de Vendas por Dia:\n")
        for dia, total in vendas_por_dia.items():
            file.write(f"{dia}: R$ {total:.2f}\n")

        file.write(f"\nTotal Geral de Vendas: R$ {total_geral:.2f}\n")

    print("Relatório de Vendas:")
    print("====================\n")

    print("Total de Vendas por Produto:")
    for produto, total in vendas_por_produto.items():
        print(f"{produto}: R$ {total:.2f}")

    print("\nTotal de Vendas por Dia:")
    for dia, total in vendas_por_dia.items():
        print(f"{dia}: R$ {total:.2f}")

    print(f"\nTotal Geral de Vendas: R$ {total_geral:.2f}")

# Verifica se o arquivo de vendas existe
if os.path.exists(arquivo_vendas):
    vendas_por_produto, vendas_por_dia, total_geral = processar_vendas(arquivo_vendas)
    gerar_relatorio(vendas_por_produto, vendas_por_dia, total_geral, arquivo_relatorio)
else:
    print(f"Erro: O arquivo '{arquivo_vendas}' não foi encontrado.")
