class Caixa:
    def __init__(self):
        self.aberto = False
        self.valor_dia_anterior = 0.0
        self.fluxo_caixa = 0.0

    def abrir_caixa(self):
        self.valor_dia_anterior = float(input("Qual o valor do dia anterior? "))
        self.aberto = True
        self.fluxo_caixa = self.valor_dia_anterior
        print("Caixa aberto.")

    def fechar_caixa(self):
        if self.aberto:
            print(f"Fluxo de caixa do dia: {self.fluxo_caixa}")
            self.aberto = False
        else:
            print("Caixa já está fechado.")