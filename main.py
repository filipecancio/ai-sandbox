from model.atendente import Atendente
from model.cor_escala import CorEscala

if __name__ == "__main__":
    atendente = Atendente("Carla")
    atendente.apresentar()
    CorEscala.RED.apresentar()
    CorEscala.GREEN.apresentar()
    CorEscala.BLUE.apresentar()
