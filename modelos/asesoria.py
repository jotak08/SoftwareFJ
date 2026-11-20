
from modelos.servicios import Servicio


class Asesoria(Servicio):

    def __init__(self, identificador, nombre, tarifa_base, especialidad):
        super().__init__(identificador, nombre, tarifa_base)

        self.especialidad = especialidad
        self.validar_parametros()

    def validar_parametros(self):
        if not isinstance(self.especialidad, str) or not self.especialidad.strip():
            raise ValueError("La especialidad es obligatoria.")

    def calcular_costo(self, duracion):
        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ValueError("La duración debe ser positiva.")

        return self.tarifa_base * duracion

    def describir(self):
        return (
            f"Servicio: {self.nombre}\n"
            f"Especialidad: {self.especialidad}\n"
            f"Tarifa por hora: ${self.tarifa_base:,.0f}"
        )

    def mostrar_informacion(self):
        return self.describir()
