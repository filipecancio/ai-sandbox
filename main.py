from model.atendente import Atendente
from model.cor_escala import CorEscala

listaCores = [CorEscala.RED, CorEscala.GREEN, CorEscala.GREY]

def declarar(cor: CorEscala):
    cor.apresentar("declarar")

if __name__ == "__main__":
    example = {
        "nome": "fulano",
        "idade": "200Anos"
    }
    print(list(example))
