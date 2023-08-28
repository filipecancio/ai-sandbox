
class Atendente:
    def __init__(self,nome) -> None:
        self.nome = nome
        
    def apresentar(self):
        print(f"boa tarde, eu sou {self.nome}")