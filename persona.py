class Persona:
    def __init__(self, nombre, documento):
        self._nombre = nombre
        self._documento = documento
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def documento(self):
        return self._documento