
class ErrorSoftwareFJ(Exception):
    """Excepción base del sistema Software FJ."""
    pass


class ReservaNoEncontradaError(ErrorSoftwareFJ):
    """Se genera cuando no existe una reserva."""
    pass


class ReservaYaConfirmadaError(ErrorSoftwareFJ):
    """Se genera cuando una reserva ya está confirmada."""
    pass


class ReservaCanceladaError(ErrorSoftwareFJ):
    """Se genera cuando se intenta operar con una reserva cancelada."""
    pass


class ClienteNoEncontradoError(ErrorSoftwareFJ):
    """Se genera cuando no existe un cliente."""
    pass
