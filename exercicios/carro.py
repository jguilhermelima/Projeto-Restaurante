from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas, cor):
        super().__init__(marca, modelo)
        self.portas = portas
        self.cor = cor

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f'carro {self.modelo} da marca {self.marca} com {self.portas} está no estado {status}'

    def ligar(self):
        pass