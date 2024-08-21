from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f'moto {self.modelo} da marca {self.marca} do tipo {self.tipo} está no estado {status}'

    def ligar(self):
        pass