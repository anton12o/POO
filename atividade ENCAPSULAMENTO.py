class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo       
        self._cor = cor            
        self.__ano = 2020           

    def mostrar_informacoes(self):
        print(f"Modelo: {self.modelo}, Cor: {self._cor}, Ano: {self.__ano}")
