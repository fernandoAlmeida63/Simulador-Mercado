from product import Produto

class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, produto):
        self.produtos[produto.codigo] = produto

    def alterar_preco(self, codigo, novo_preco):
        if codigo in self.produtos:
            self.produtos[codigo].preco = novo_preco
            print(f"Preço do produto {codigo} alterado para {novo_preco}.")

    def atualizar_estoque(self, codigo, quantidade):
        if codigo in self.produtos:
            self.produtos[codigo].quantidade += quantidade
            print(f"Estoque do produto {codigo} atualizado. Nova quantidade: {self.produtos[codigo].quantidade}.")

    def desativar_produto(self, codigo):
        if codigo in self.produtos:
            self.produtos[codigo].desativar()
            print(f"Produto {codigo} desativado.")

    def pesquisar_produto(self, codigo):
        return self.produtos.get(codigo)

    def relatorio_vencimento(self, dias):
        return [produto for produto in self.produtos.values() if produto.validade <= dias and produto.ativo]

    def relatorio_quantidade_para_compra(self):
        return {produto.nome: produto.quantidade for produto in self.produtos.values() if produto.quantidade < 5 and produto.ativo}
    