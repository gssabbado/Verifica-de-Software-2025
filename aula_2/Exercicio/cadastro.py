class Cadastro:
    def __init__(self, idade, categoria, tempoEstimado, assinaturaTermo):
        self.idade = idade
        self.categoria = categoria
        self.tempoEstimado = tempoEstimado
        self.assinaturaTermo = assinaturaTermo

    def get(self):
        return {
            "idade": self.idade,
            "categoria": self.categoria,
            "tempoEstimado": self.tempoEstimado,
            "assinaturaTermo": self.assinaturaTermo
        }