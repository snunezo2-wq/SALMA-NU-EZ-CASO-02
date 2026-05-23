from modelo.turno import Turno

class CajaAtencion:
    def __init__(self):
        self._turnos = []
        self._contador = 0
    
    def agregar_persona(self, persona):
        self._contador += 1
        nuevo_turno = Turno(persona, self._contador)
        self._turnos.append(nuevo_turno)
        print(f"Turno #{nuevo_turno.numero} asignado a {persona.nombre}")
    
    def atender_siguiente(self):
        if self.esta_vacia():
            print("No hay nadie en la cola")
            return None
        
        # sacamos al primero que llegó (comportamiento FIFO)
        turno_atendido = self._turnos.pop(0)
        print(f"Atendiendo a {turno_atendido.persona.nombre} (Turno #{turno_atendido.numero})")
        return turno_atendido
    
    def esta_vacia(self):
        return len(self._turnos) == 0
    
    def proximo_turno(self):
        if self.esta_vacia():
            print("Cola vacía")
            return None
        siguiente = self._turnos[0]
        print(f"Próximo turno: #{siguiente.numero} - {siguiente.persona.nombre}")
        return siguiente