class Cliente:
    def __init__(self, nome, login, senha):
        self.nome = nome
        self.login = login
        self.senha = senha
    
    def cadastrar_cliente(self):
        self.nome = input("Nome: ")
        self.login = input("Login: ")
        self.senha = input("Senha: ")
    
    def exibir_cliente(self):
        print(f"Nome: {self.nome}")
        print(f"Login: {self.login}")
        print(f"Senha: {self.senha}")