def cantidad():
    print("digite la cantidad de numeros que desea sumar: ")
    cantidad = int(input())
    return cantidad

def sumatoria(cantidad):
    suma = 0
    for i in range(cantidad):
        numero = int(input(f"Digite el número {i+1}: "))
        suma = suma + numero
    return suma
     
def mensaje(resultado):  
    print("La sumatoria es:", resultado)
     
#Codigo principal

dato_cantidad = cantidad()
dato_suma = sumatoria(dato_cantidad)
mensaje(dato_suma)
    