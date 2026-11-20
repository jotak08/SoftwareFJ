
from configuracion import logger


print("\n===== PRUEBA TRY / EXCEPT =====")

try:
    resultado = 10 / 0

except ZeroDivisionError as error:
    print("Error controlado:", error)
    logger.error(f"Error de división: {error}")


print("\n===== PRUEBA TRY / EXCEPT / ELSE =====")

try:
    resultado = 100 / 5

except ZeroDivisionError as error:
    print("Error:", error)

else:
    print("Operación exitosa. Resultado:", resultado)


print("\n===== PRUEBA TRY / EXCEPT / FINALLY =====")

try:
    archivo = open("prueba.txt", "w", encoding="utf-8")
    archivo.write("Prueba de manejo de excepciones.")

except OSError as error:
    print("Error al trabajar con el archivo:", error)

finally:
    if "archivo" in locals():
        archivo.close()

    print("Bloque finally ejecutado.")


print("\n===== PRUEBA DE ENCADENAMIENTO =====")

try:
    try:
        numero = int("Software FJ")

    except ValueError as error:
        raise RuntimeError(
            "No fue posible convertir el dato a número."
        ) from error

except RuntimeError as error:
    print("Error controlado:", error)
    print("Causa original:", error.__cause__)
    logger.exception("Error durante la conversión de datos.")


print("\nEl programa continúa funcionando.")
