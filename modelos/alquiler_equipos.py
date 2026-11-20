
from modelos.servicios import Servicio


class AlquilerEquipo(Servicio):

    def __init__(self, identificador, nombre, tarifa_base, cantidad):
        super().__init__(identificador, nombre, tarifa_base)

        self.cantidad = cantidad
        self.validar_parametros()

    def validar_parametros(self):
        if isinstance(self.cantidad, bool) or not isinstance(self.cantidad, int):
            raise ValueError("La cantidad debe ser un número entero.")

        if self.cantidad <= 0:
            raise ValueError("Debe alquilar al menos un equipo.")

    def calcular_costo(self, duracion):
        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ValueError("La duración debe ser positiva.")

        return self.tarifa_base * duracion * self.cantidad

    def describir(self):
        return (
            f"Servicio: {self.nombre}\n"
            f"Cantidad de equipos: {self.cantidad}\n"
            f"Tarifa diaria por equipo: ${self.tarifa_base:,.0f}"
        )

    def mostrar_informacion(self):
        return self.describir()
