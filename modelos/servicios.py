
from abc import ABC, abstractmethod 
from modelos.entidad import Entidad


class Servicio(Entidad):
    """
    Clase abstracta que representa un servicio
    ofrecido por Software FJ.
    """

    def __init__(self, identificador, nombre, tarifa_base):
        super().__init__(identificador)

        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del servicio es obligatorio.")

        if isinstance(tarifa_base, bool) or not isinstance(tarifa_base, (int, float)) or tarifa_base <= 0:
            raise ValueError("La tarifa debe ser un número positivo.")

        self.nombre = nombre.strip()
        self.tarifa_base = tarifa_base

    @abstractmethod
    def calcular_costo(self, duracion):
        """Calcula el costo según el tipo de servicio."""
        pass

    @abstractmethod
    def describir(self):
        """Devuelve una descripción del servicio."""
        pass

    @abstractmethod
    def validar_parametros(self):
        """Valida los datos particulares del servicio."""
        pass
