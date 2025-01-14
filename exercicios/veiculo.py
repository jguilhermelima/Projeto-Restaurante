from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca= marca
        self.modelo = modelo
        self._ligado = False


    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f'carro {self.modelo} da marca {self.marca} está no estado {status}'
    
    @abstractmethod
    def ligar(self):
        pass

    