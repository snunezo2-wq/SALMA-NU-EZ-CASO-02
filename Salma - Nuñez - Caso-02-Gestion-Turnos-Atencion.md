# 🕒 Caso de Estudio 02: Gestión de Turnos de Atención

## Información General

| Campo | Detalle |
|------|---------|
| Asignatura | Programación Orientada a Objetos |
| Duración | 20 minutos |
| Nivel | Básico |
| Herramientas | Python 3.10+, editor de texto/IDE |

## Contexto
La oficina de atención al estudiante asigna turnos a las personas que llegan. Cada persona recibe un ticket y espera en una fila hasta ser atendida. El sistema debe registrar la llegada, atender en orden FIFO y mostrar quién sigue.

## Objetivo
Construir un modelo de clases que represente personas, turnos y la cola de atención, luego implementarlo en Python.

## Estructura de directorios sugerida
- `modelo/`
  - `persona.py`
  - `turno.py`
  - `caja_atencion.py`
- `uml/`
  - `caso_05_turnos.puml`
- `main.py`

## 1. Análisis / Abstracción

### Narrativa
- Cada persona tiene nombre y documento.
- Al llegar, se crea un turno con número consecutivo.
- La caja de atención atiende a la primera persona que llegó.
- Se puede consultar si hay alguien esperando.

### Tareas de análisis
- Identifica entidades: persona, turno, caja de atención.
- Lista atributos de cada entidad.
- Define operaciones principales.

### Entidades sugeridas
- `Persona` → nombre, documento
- `Turno` → persona, número de turno
- `CajaAtencion` → lista de turnos pendientes

## 2. Diseño / Modelado de clases

### Relaciones
- `Turno` referencia a `Persona`.
- `CajaAtencion` contiene turnos en una lista interna.

### Clases mínimas
- `Persona`
- `Turno`
- `CajaAtencion`

### Métodos propuestos
- `CajaAtencion.agregar_persona(persona)`
- `CajaAtencion.atender_siguiente()`
- `CajaAtencion.esta_vacia()`
- `CajaAtencion.proximo_turno()`

## 3. Implementación en Python

### Requisitos mínimos
- Usa clases con atributos privados y propiedades.
- Implementa la cola como una lista interna en `CajaAtencion`.
- Modela las clases UML en PlanTUML antes de codificar.
- El método `atender_siguiente()` debe extraer el primer turno.

### `main.py` debe:
- crear 4 personas,
- registrar su llegada en la `CajaAtencion`,
- atender a 2 personas,
- mostrar el siguiente turno en espera.

### Preguntas de comprobación
- ¿Por qué el turno se modela como objeto separado?
- ¿Qué operación representa el comportamiento FIFO?
- ¿Qué ocurre si no hay más personas en la cola?

---

## Resultado esperado
Un programa Python que simula atención en orden de llegada, con clases claramente separadas y comportamiento FIFO.
