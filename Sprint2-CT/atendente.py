import random

class Atendente:
    def __init__(self, nome):
        self.nome = nome
        
        
class CentralAtendimento:
    def __init__(self):
        self.atendentes = [
            Atendente("Luis Fernando"),
            Atendente("Gabriel"),
            Atendente("Felipe"),
            Atendente("Murilo")
        ]
        
    def escolher_atendente(self):
        atendente_escolhido = random.choice(self.atendentes)
        return atendente_escolhido
        
central = CentralAtendimento()
atendente = central.escolher_atendente()