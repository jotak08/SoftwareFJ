
from modelos.servicios import Servicio


class ReservaSala(Servicio):

    def __init__(self, identificador, nombre, tarifa_base, capacidad):
        super().__init__(identificador, nombre, tarifa_base)

        self.capacidad = capacidad
        self.validar_parametros()

    def validar_parametros(self):
        if isinstance(self.capacidad, bool) or not isinstance(self.capacidad, int):
            raise ValueError("La capacidad debe ser un número entero.")

        if self.capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor que cero.")

    def calcular_costo(self, duracion):
        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ValueError("La duración debe ser positiva.")

        return self.tarifa_base * duracion

    def describir(self):
        return (
            f"Servicio: {self.nombre}\n"
            f"Capacidad: {self.capacidad} personas\n"
            f"Tarifa por hora: ${self.tarifa_base:,.0f}"
        )

    def mostrar_informacion(self):
        return self.describir()
