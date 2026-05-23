from modelo.persona import Persona
from modelo.caja_atencion import CajaAtencion

def main():
    caja = CajaAtencion()
    
    # Crear 4 personas
    personas = [
        Persona("Carlos Pérez", "1204567822"),
        Persona("Luisa Jimenez", "0965432112"),
        Persona("Javier Ortega", "1122334450"),
        Persona("Roberto Saltos", "1724332211")
    ]
    
    # Registrar llegadas
    print("--- Llegada de personas ---")
    for persona in personas:
        caja.agregar_persona(persona)
    
    print("\n--- Mostrar próximo turno ---")
    caja.proximo_turno()
    
    # Atender de 2 en 2 hasta que la cola esté vacía
    grupo = 1
    while not caja.esta_vacia():
        print(f"\n--- Atendiendo grupo {grupo} (2 personas) ---")
        
        # Atender hasta 2 personas (o las que queden)
        for _ in range(2):
            if caja.esta_vacia():
                break
            caja.atender_siguiente()
        
        if not caja.esta_vacia():
            print("\n--- Próximo turno después del grupo ---")
            caja.proximo_turno()
        else:
            print("\n--- Todas las personas han sido atendidas ---")
            caja.proximo_turno()
        
        grupo += 1

if __name__ == "__main__":
    main()