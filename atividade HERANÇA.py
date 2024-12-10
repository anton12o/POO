class Veiculo:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor

    def mover(self):
        print("O veículo está se movendo.")

class Carro(Veiculo):  
    def __init__(self, modelo, cor, num_portas):
        super().__init__(modelo, cor)  
        self.num_portas = num_portas
