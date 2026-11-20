
from gestion.reserva import Reserva
from excepciones.errores import ReservaNoEncontradaError
from configuracion import logger


class GestorReservas:

    def __init__(self):
        self.reservas = []

    
    def registrar_reserva(self, reserva):

        if not isinstance(reserva, Reserva):
            raise TypeError("Solo se pueden registrar objetos Reserva.")

        for reserva_existente in self.reservas:
            if reserva_existente.identificador == reserva.identificador:
                logger.warning(
                    f"Intento de registrar una reserva duplicada: {reserva.identificador}"
                )
                raise ValueError(
                    f"Ya existe una reserva con ID {reserva.identificador}."
                )

        self.reservas.append(reserva)

        logger.info(
            f"Reserva {reserva.identificador} registrada correctamente."
        )

        return "Reserva registrada correctamente."


        
    def buscar_reserva(self, identificador, estado=None):

        for reserva in self.reservas:

            if reserva.identificador == identificador:

                # Si no se especifica estado, devuelve la reserva
                if estado is None:
                    return reserva

                # Si se especifica estado, también lo verifica
                if reserva.estado == estado:
                    return reserva

        # Si no se encontró la reserva o no coincide el estado
        if estado is None:
            raise ReservaNoEncontradaError(
                f"No se encontró la reserva con ID {identificador}."
            )

        raise ReservaNoEncontradaError(
            f"No se encontró una reserva con ID {identificador} "
            f"y estado {estado}."
        )


    def listar_reservas(self):
        if not self.reservas:
            return "No hay reservas registradas."

        informacion = []

        for reserva in self.reservas:
            informacion.append(reserva.mostrar_informacion())

        return "\n\n".join(informacion)

    def confirmar_reserva(self, identificador):
        reserva = self.buscar_reserva(identificador)
        return reserva.confirmar()

    def cancelar_reserva(self, identificador):
        reserva = self.buscar_reserva(identificador)
        return reserva.cancelar()

    def procesar_reserva(self, identificador):
        reserva = self.buscar_reserva(identificador)
        return reserva.procesar()   
