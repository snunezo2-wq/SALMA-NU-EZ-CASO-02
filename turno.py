from modelo.persona import Persona

class Turno:
    def __init__(self, persona, numero):
        self._persona = persona
        self._numero = numero
    
    @property
    def persona(self):
        return self._persona
    
    @property
    def numero(self):
        return self._numero