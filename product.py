class Produto:
    def __init__(self, codigo, nome, tipo, validade=None, garantia=None, preco=0.0, quantidade=0):
        self.codigo = codigo
        self.nome = nome
        self.tipo = tipo  # 'alimento' ou 'eletrodoméstico'
        self.validade = validade  # em dias, se for alimento
        self.garantia = garantia  # em meses, se for eletrodoméstico
        self.preco = preco
        self.quantidade = quantidade
        self.ativo = True  # Para desativar o produto

    def desativar(self):
        self.ativo = False