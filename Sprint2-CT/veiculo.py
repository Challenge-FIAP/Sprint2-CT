class Veiculo:
    def __init__(self, modelo, marca, placa, tipo):
        self.modelo = modelo
        self.marca = marca
        self.placa = placa
        self.tipo = tipo
    
    def cadastrar_veiculo(self):
        self.modelo = input("Digite o modelo do veículo: ")
        self.marca = input("Digite a marca do veículo: ")
        self.placa = input("Digite a placa do veículo: ")
        
        print("Selecione o tipo de veículo:")
        print("1 - Moto")
        print("2 - Veículo de passeio")
        print("3 - Veículo de carga leve")
        print("4 - Veículo de carga pesado")
        print("5 - Outros")
        
        opcao = int(input("Digite o número correspondente ao tipo de veículo: "))
        
        if opcao == 1:
            self.tipo = "Moto"
        elif opcao == 2:
            self.tipo = "Veículo de passeio"
        elif opcao == 3:
            self.tipo = "Veículo de carga leve"
        elif opcao == 4:
            self.tipo = "Veículo de carga pesado"
        else:
            self.tipo = "Outros"
    
    def exibir_veiculo(self):
        print(f"Modelo: {self.modelo}")
        print(f"Marca: {self.marca}")
        print(f"Placa: {self.placa}")
        print(f"Tipo: {self.tipo}")
