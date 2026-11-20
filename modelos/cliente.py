
from modelos.entidad import Entidad


class Cliente(Entidad):

    def __init__(self, identificador, nombre, correo, telefono):
        super().__init__(identificador)

        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    # Validación y encapsulación del nombre
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")

        self.__nombre = valor.strip()

    # Validación y encapsulación del correo
    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):
        if not isinstance(valor, str) or "@" not in valor or "." not in valor:
            raise ValueError("El correo electrónico no es válido.")

        self.__correo = valor.strip()

    # Validación y encapsulación del teléfono
    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):
        if not isinstance(valor, str) or not valor.isdigit():
            raise ValueError("El teléfono debe contener solo números.")

        if not 7 <= len(valor) <= 15:
            raise ValueError("La longitud del teléfono no es válida.")

        self.__telefono = valor

    # Implementación del método abstracto
    def mostrar_informacion(self):
        return (
            f"ID: {self.identificador}\n"
            f"Nombre: {self.nombre}\n"
            f"Correo: {self.correo}\n"
            f"Teléfono: {self.telefono}"
        )
