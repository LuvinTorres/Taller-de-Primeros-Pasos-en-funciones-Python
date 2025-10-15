# ***** Estructura del switch - match *****

#  Función para pedir el número al usuario
def pedir_numero():
    num = int(input("Digite un número del 1 al 12: "))
    return num

# Función para obtener el nombre del mes usando match-case
def obtener_mes(num):
    match num:
        case 1:
            return "Enero"
        case 2:
            return "Febrero"
        case 3:
            return "Marzo"
        case 4:
            return "Abril"
        case 5:
            return "Mayo"
        case 6:
            return "Junio"
        case 7:
            return "Julio"
        case 8:
            return "Agosto"
        case 9:
            return "Septiembre"
        case 10:
            return "Octubre"
        case 11:
            return "Noviembre"
        case 12:
            return "Diciembre"
        case _:
            return "Número inválido, debe estar entre 1 y 12"


def main():
    numero = pedir_numero()
    mes = obtener_mes(numero)
    print("El mes correspondiente es:", mes)

# codigo principal
main()