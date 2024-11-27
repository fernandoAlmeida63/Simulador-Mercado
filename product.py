import json

class Produto:
    def __init__(self, codigo, nome, tipo, validade, garantia, preco, quantidade, ativo):
        self.codigo = codigo
        self.nome = nome
        self.tipo = tipo
        self.validade = validade
        self.garantia = garantia
        self.preco = preco
        self.quantidade = quantidade
        self.ativo = ativo

def carregar_estoque():
    try:
        with open('caminho/para/seu/arquivo.json', 'r') as f:
            produtos_data = json.load(f)
            produtos = []
            for produto_id, produto_data in produtos_data.items():
                produto = Produto(**produto_data)  # Desempacotando o dicionário
                produtos.append(produto)
            return produtos
    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o caminho.")
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")
    except TypeError as e:
        print(f"Erro de tipo: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Chame a função
estoque = carregar_estoque()