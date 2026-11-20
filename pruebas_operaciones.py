
from modelos.cliente import Cliente
from modelos.reserva_salas import ReservaSala
from gestion.reserva import Reserva
from gestion.reservas import GestorReservas

from excepciones.errores import (
    ReservaNoEncontradaError,
    ReservaYaConfirmadaError,
    ReservaCanceladaError
)


# Preparar los objetos para las pruebas

cliente = Cliente(
    1,
    "Carlos Ramirez",
    "carlos@gmail.com",
    "3001234567"
)

sala = ReservaSala(
    101,
    "Sala de reuniones",
    50000,
    20
)

reserva1 = Reserva(1, cliente, sala, 3)
reserva2 = Reserva(2, cliente, sala, 2)

gestor = GestorReservas()


print("\n===== DIEZ OPERACIONES SIMULADAS =====")


# OPERACIÓN 1: Registrar una reserva correctamente
print("\n1. Registrar reserva válida")

try:
    print(gestor.registrar_reserva(reserva1))
except Exception as error:
    print("Error:", error)


# OPERACIÓN 2: Buscar una reserva existente
print("\n2. Buscar reserva existente")

try:
    encontrada = gestor.buscar_reserva(1)
    print("Reserva encontrada:", encontrada.identificador)
except ReservaNoEncontradaError as error:
    print("Error:", error)


# OPERACIÓN 3: Confirmar una reserva pendiente
print("\n3. Confirmar reserva")

try:
    print(gestor.confirmar_reserva(1))
except Exception as error:
    print("Error:", error)


# OPERACIÓN 4: Intentar confirmar nuevamente
print("\n4. Confirmar una reserva ya confirmada")

try:
    gestor.confirmar_reserva(1)
except ReservaYaConfirmadaError as error:
    print("Error controlado:", error)


# OPERACIÓN 5: Procesar una reserva confirmada
print("\n5. Procesar reserva")

try:
    print(gestor.procesar_reserva(1))
except Exception as error:
    print("Error:", error)


# OPERACIÓN 6: Intentar procesar nuevamente
print("\n6. Procesar una reserva ya procesada")

try:
    gestor.procesar_reserva(1)
except ValueError as error:
    print("Error controlado:", error)


print("\n6.1 Confirmar una reserva ya procesada")

try:
    gestor.confirmar_reserva(1)

except ValueError as error:
    print(f"Error controlado: {error}")


# OPERACIÓN 7: Buscar una reserva inexistente
print("\n7. Buscar reserva inexistente")

try:
    gestor.buscar_reserva(999)
except ReservaNoEncontradaError as error:
    print("Error controlado:", error)


# OPERACIÓN 8: Registrar una reserva duplicada
print("\n8. Registrar una reserva con ID duplicado")

try:
    gestor.registrar_reserva(reserva1)
except ValueError as error:
    print("Error controlado:", error)


# OPERACIÓN 9: Registrar y cancelar otra reserva
print("\n9. Registrar y cancelar una reserva")

try:
    print(gestor.registrar_reserva(reserva2))
    print(gestor.cancelar_reserva(2))
    print("Estado:", reserva2.estado)
except Exception as error:
    print("Error:", error)


# OPERACIÓN 10: Intentar procesar una reserva cancelada
print("\n10. Procesar una reserva cancelada")

try:
    gestor.procesar_reserva(2)
except ReservaCanceladaError as error:
    print("Error controlado:", error)


# PRUEBA ADICIONAL: Buscar con diferentes argumentos

print("\n===== PRUEBA DE SOBRECARGA =====")

try:
    # Primera forma: buscar por ID
    resultado1 = gestor.buscar_reserva(1)
    print("Búsqueda por ID:", resultado1.estado)

    # Segunda forma: buscar por ID y estado
    resultado2 = gestor.buscar_reserva(1, "Procesada")
    print("Búsqueda por ID y estado:", resultado2.estado)

except ReservaNoEncontradaError as error:
    print("Error controlado:", error)



print("\n===== PRUEBAS FINALIZADAS =====")
print("El sistema continúa funcionando.")
