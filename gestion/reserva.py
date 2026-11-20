
from modelos.cliente import Cliente
from modelos.servicios import Servicio
from excepciones.errores import (
    ReservaYaConfirmadaError,
    ReservaCanceladaError
)
from configuracion import logger


class Reserva:

    def __init__(self, identificador, cliente, servicio, duracion):

        if not identificador:
            raise ValueError("El identificador de la reserva es obligatorio.")

        if not isinstance(cliente, Cliente):
            raise TypeError("La reserva requiere un objeto Cliente.")

        if not isinstance(servicio, Servicio):
            raise TypeError("La reserva requiere un objeto Servicio.")

        if (
            isinstance(duracion, bool)
            or not isinstance(duracion, (int, float))
            or duracion <= 0
        ):
            raise ValueError("La duración debe ser un número positivo.")

        self.identificador = identificador
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    
    def confirmar(self):

        if self.estado == "Confirmada":
            raise ReservaYaConfirmadaError(
                f"La reserva {self.identificador} ya está confirmada."
            )

        if self.estado == "Cancelada":
            raise ReservaCanceladaError(
                f"No se puede confirmar la reserva {self.identificador} porque está cancelada."
            )

        if self.estado == "Procesada":
            raise ValueError(
                f"No se puede confirmar la reserva {self.identificador} porque ya fue procesada."
            )

        self.estado = "Confirmada"

        logger.info(
            f"Reserva {self.identificador} confirmada."
        )

        return "Reserva confirmada correctamente."

    
    def cancelar(self):

        if self.estado == "Cancelada":
            raise ReservaCanceladaError(
                f"La reserva {self.identificador} ya está cancelada."
            )

        if self.estado == "Confirmada":
            raise ReservaYaConfirmadaError(
                f"No se puede cancelar la reserva {self.identificador} porque está confirmada."
            )

        if self.estado == "Procesada":
            raise ValueError(
                "No se puede cancelar una reserva que ya fue procesada."
            )

        self.estado = "Cancelada"

        logger.info(
            f"Reserva {self.identificador} cancelada."
        )

        return "Reserva cancelada correctamente."


    
    def procesar(self):

        if self.estado == "Pendiente":
            raise ValueError(
                "No se puede procesar una reserva pendiente. Primero debe confirmarse."
            )

        if self.estado == "Cancelada":
            raise ReservaCanceladaError(
                "No se puede procesar una reserva cancelada."
            )

        if self.estado == "Procesada":
            raise ValueError(
                "Esta reserva ya fue procesada."
            )

        if self.estado == "Confirmada":
            self.estado = "Procesada"
            logger.info(f"Reserva {self.identificador} procesada.")
            return "Reserva procesada correctamente."

    def calcular_total(self):
        return self.servicio.calcular_costo(self.duracion)

    def mostrar_informacion(self):
        return (
            f"===== RESERVA {self.identificador} =====\n"
            f"Cliente: {self.cliente.nombre}\n"
            f"Correo: {self.cliente.correo}\n"
            f"Servicio: {self.servicio.nombre}\n"
            f"Duración: {self.duracion}\n"
            f"Estado: {self.estado}\n"
            f"Total: ${self.calcular_total():,.0f}"
        )
