
# ==========================================
# IMPORTACIONES
# ==========================================

from modelos.cliente import Cliente
from modelos.reserva_salas import ReservaSala
from modelos.alquiler_equipos import AlquilerEquipo
from modelos.asesoria import Asesoria

from gestion.reserva import Reserva
from gestion.reservas import GestorReservas

from excepciones.errores import (
    ReservaNoEncontradaError,
    ReservaYaConfirmadaError
)


# ==========================================
# 1. REGISTRO Y VALIDACIÓN DE CLIENTE
# ==========================================

cliente1 = Cliente(
    1,
    "Carlos Ramírez",
    "carlos@gmail.com",
    "3001234567"
)

print("=== CLIENTE REGISTRADO ===")
print(cliente1.mostrar_informacion())


print("\n=== PRUEBA DE VALIDACIÓN ===")

try:
    cliente1.correo = "correo_invalido"

except ValueError as error:
    print(f"Error controlado: {error}")

print("\nEl programa continúa funcionando.")


# ==========================================
# 2. CREACIÓN DE SERVICIOS
# ==========================================

sala = ReservaSala(
    101,
    "Sala de reuniones",
    50000,
    20
)

equipo = AlquilerEquipo(
    102,
    "Computadores portátiles",
    30000,
    2
)

asesoria = Asesoria(
    103,
    "Asesoría tecnológica",
    80000,
    "Desarrollo de software"
)


# ==========================================
# 3. PRUEBA DE POLIMORFISMO
# ==========================================

servicios = [sala, equipo, asesoria]

print("\n===== SERVICIOS SOFTWARE FJ =====")

for servicio in servicios:

    print("\n" + servicio.describir())

    costo = servicio.calcular_costo(3)

    print(f"Costo total: ${costo:,.0f}")


# ==========================================
# 4. CREACIÓN DE UNA RESERVA
# ==========================================

reserva1 = Reserva(
    1,
    cliente1,
    sala,
    3
)

print("\n===== PRUEBA DE RESERVA =====")
print(reserva1.mostrar_informacion())


# ==========================================
# 5. CONFIRMACIÓN DE RESERVA
# ==========================================

print("\n===== CONFIRMACIÓN DE RESERVA =====")

print(reserva1.confirmar())
print("Nuevo estado:", reserva1.estado)


# Intentar confirmar nuevamente
print("\n===== PRUEBA DE EXCEPCIÓN =====")

try:
    reserva1.confirmar()

except ReservaYaConfirmadaError as error:
    print(f"Error controlado: {error}")


# ==========================================
# 6. GESTIÓN DE RESERVAS
# ==========================================

gestor = GestorReservas()

print("\n===== GESTIÓN DE RESERVAS =====")

try:
    print(gestor.registrar_reserva(reserva1))

except ValueError as error:
    print(f"Error controlado: {error}")


# ==========================================
# 7. LISTADO DE RESERVAS
# ==========================================

print("\n===== LISTADO DE RESERVAS =====")
print(gestor.listar_reservas())


# ==========================================
# 8. BÚSQUEDA DE RESERVA
# ==========================================

print("\n===== BÚSQUEDA DE RESERVA =====")

try:
    reserva_encontrada = gestor.buscar_reserva(1)
    print(reserva_encontrada.mostrar_informacion())

except ReservaNoEncontradaError as error:
    print(f"Error controlado: {error}")


# ==========================================
# 9. BÚSQUEDA DE RESERVA INEXISTENTE
# ==========================================

print("\n===== PRUEBA DE RESERVA INEXISTENTE =====")

try:
    gestor.buscar_reserva(999)

except ReservaNoEncontradaError as error:
    print(f"Error controlado: {error}")


# ==========================================
# 10. PROCESAMIENTO DE RESERVA
# ==========================================

print("\n===== PROCESAMIENTO DE RESERVA =====")

try:
    print(gestor.procesar_reserva(1))
    print("Nuevo estado:", reserva1.estado)

except (ValueError, ReservaNoEncontradaError) as error:
    print(f"Error controlado: {error}")


print("\n===== FIN DEL PROGRAMA =====")
print("El sistema Software FJ continúa funcionando correctamente.")
