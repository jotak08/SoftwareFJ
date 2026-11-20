from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta que representa una entidad general
    dentro del sistema Software FJ.
    """

    def __init__(self, identificador):
        if not identificador:
            raise ValueError("El identificador es obligatorio.")

        self.identificador = identificador

    @abstractmethod
    def mostrar_informacion(self):
        """
        Método abstracto que deben implementar
        las clases que hereden de Entidad.
        """
        pass
