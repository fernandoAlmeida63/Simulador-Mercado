from stock import Estoque

class Venda:
    def __init__(self, estoque):
        self.estoque = estoque
        self.itens = []
        self.subtotal = 0.0

    def abrir_venda(self):
        while True:
            codigo = input("Digite o código do produto (ou 'sair' para finalizar): ")
            if codigo == 'sair':
                break
            quantidade = int(input("Digite a quantidade: "))
            produto = self.estoque.pesquisar_produto(codigo)
            if produto and produto.ativo and produto.quantidade >= quantidade:
                self.itens.append((produto, quantidade))
                self.subtotal += produto.preco * quantidade
                produto.quantidade -= quantidade
            else:
                print("Produto não disponível ou quantidade insuficiente.")

    def excluir_item(self, codigo):
        for item in self.itens:
            if item[0].codigo == codigo:
                self.itens.remove(item)
                self.subtotal -= item[0].preco * item[1]
                item[0].quantidade += item[1]  # Retorna a quantidade ao estoque
                print(f"Item {item[0].nome} removido da venda.")
                break

    def mostrar_subtotal(self):
        print(f"Subtotal: {self.subtotal}")

    def lista_agrupada(self):
        print("Itens vendidos:")
        for produto, quantidade in self.itens:
            print(f"{produto.nome} - Quantidade: {quantidade}")