class Carro:
     def __init__(self,marca, modelo)
        self.marca = marca 
        self.modelo = modelo

    def exibir_info(self):
        return f"Marca: {self.marca}, modelo: 
{self.modelo}"
meu_carro = Carro ("Renault", "clio")
print(meu_carr0.exibir_info())

class CarroEletrico(carro)
      def __init__(self, marca, modelo, 
autonomia_bateria):
      super().__init__(self, marca, modelo)
      self.autonomia = autonomia_bateria
      delf exibir_info(self)
      info_base = super (). exibir_info()
      return f"{info_base} ||Autonomia da 
Bateria: {self.autonomia} km"

meu_carro = CarroEletrico("BYD", "Dolphin",
600)
print(meu_carro.exibir_info())