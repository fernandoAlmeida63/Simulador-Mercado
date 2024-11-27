import json
from stock import Estoque
from Box import Caixa
from Sales import Venda
from product import Produto

def salvar_estoque(estoque, filename='estoque.json'):
    with open(filename, 'w') as f:
        json.dump({codigo: produto.__dict__ for codigo, produto in estoque.produtos.items()}, f)

def carregar_estoque(filename='estoque.json'):
    estoque = Estoque()
    try:
        with open(filename, 'r') as f:
            produtos_data = json.load(f)
            for codigo, produto_data in produtos_data.items():
                produto = Produto(**produto_data)
                estoque.adicionar_produto(produto)
    except FileNotFoundError:
        print("Arquivo de estoque não encontrado. Um novo estoque será criado.")
    return estoque

def gerenciar_produtos(estoque):
    while True:
        print("\nGerenciamento de Produtos:")
        print("1. Adicionar produto ao estoque")
        print("2. Alterar preço de produto")
        print("3. Atualizar quantidade de produto")
        print("4. Desativar produto")
        print("5. Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            try:
                codigo = input("Digite o código do produto: ")
                nome = input("Digite o nome do produto: ")
                tipo = input("Digite o tipo do produto (alimento/eletrodoméstico): ")
                validade = int(input("Digite a validade em dias (ou 0 se não for alimento): "))
                garantia = int(input("Digite a garantia em meses (ou 0 se não for eletrodoméstico): "))
                preco = float(input("Digite o preço do produto: "))
                quantidade = int(input("Digite a quantidade do produto: "))
                estoque.adicionar_produto(Produto(codigo, nome, tipo,
                                                   validade if tipo == 'alimento' else None,
                                                   garantia if tipo == 'eletrodoméstico' else None,
                                                   preco, quantidade))
                print(f"Produto {nome} adicionado com sucesso ao estoque.")
            except ValueError:
                print("Erro: Entrada inválida. Tente novamente.")

        elif opcao == '2':
            try:
                codigo = input("Digite o código do produto: ")
                novo_preco = float(input("Digite o novo preço: "))
                estoque.alterar_preco(codigo, novo_preco)
                print(f"Preço do produto {codigo} alterado para {novo_preco}.")
            except ValueError:
                print("Erro: Entrada inválida. Tente novamente.")

        elif opcao == '3':
            try:
                codigo = input("Digite o código do produto: ")
                quantidade = int(input("Digite a quantidade a ser adicionada: "))
                estoque.atualizar_estoque(codigo, quantidade)
                print(f"Quantidade do produto {codigo} atualizada para {quantidade}.")
            except ValueError:
                print("Erro: Entrada inválida. Tente novamente.")

        elif opcao == '4':
            codigo = input("Digite o código do produto: ")
            estoque.desativar_produto(codigo)
            print(f"Produto {codigo} desativado com sucesso.")

        elif opcao == '5':
            break  # Volta ao menu principal

        else:
            print("Opção inválida. Tente novamente.")

def gerenciar_relatorios(estoque):
    while True:
        print("\nSubmenu de Relatórios:")
        print("1. Relatório de produtos prestes a vencer")
        print("2. Relatório de produtos abaixo da quantidade mínima")
        print("3. Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            dias = int(input("Digite o número de dias para verificar a validade: "))
            produtos_vencendo = estoque.relatorio_vencimento(dias)
            if produtos_vencendo:
                print("Produtos prestes a vencer:")
                for produto in produtos_vencendo:
                    print(f"{produto.nome} (Código: {produto.codigo}, Validade: {produto.validade} dias)")
            else:
                print("Nenhum produto prestes a vencer encontrado.")

        elif opcao == '2':
            quantidade_minima = int(input("Digite a quantidade mínima: "))
            produtos_baixa_quantidade = estoque.relatorio_quantidade(quantidade_minima)
            if produtos_baixa_quantidade:
                print("Produtos abaixo da quantidade mínima:")
                for produto in produtos_baixa_quantidade:
                    print(f"{produto.nome} (Código: {produto.codigo}, Quantidade: {produto.quantidade})")
            else:
                print("Nenhum produto abaixo da quantidade mínima encontrado.")

        elif opcao == '3':
            break  # Volta ao menu principal

        else:
            print("Opção inválida. Tente novamente.")

def main():
    estoque = carregar_estoque()
    caixa = Caixa()
    caixa_aberto = False  # Variável para controlar o estado do caixa

    # Menu de opções
    while True:
        print("\nMenu:")
        print("1. Gerenciar produtos")
        print("2. Abrir caixa")
        print("3. Realizar venda")
        print("4. Gerenciar relatórios")
        print("5. Fechar caixa")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            gerenciar_produtos(estoque)

        elif opcao == '2':
            caixa.abrir_caixa()
            caixa_aberto = True  # O caixa foi aberto
            print("Caixa aberto com sucesso.")

        elif opcao == '3':
            if not caixa_aberto:
                print("Erro: O caixa deve ser aberto antes de realizar vendas.")
                continue  # Retorna ao menu principal

            venda = Venda(estoque)
            venda.abrir_venda()
            venda.mostrar_subtotal()
            venda.lista_agrupada()

        elif opcao == '4':
            gerenciar_relatorios(estoque)

        elif opcao == '5':
            caixa.fechar_caixa()
            caixa_aberto = False  # O caixa foi fechado
            print("Caixa fechado com sucesso.")

        elif opcao == '6':
            salvar_estoque(estoque)
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()