# Funciones 
def dato_n():
  dato_n = int(input("escriba un numero"))
  return dato_n

def funcion_datos(dato_n):
    if dato_n >0:
        mensaje= "el numero es positivo"
    elif dato_n <0:
        mensaje="el numero es negativo"
    else:
        mensaje="el numero es cero"
    return mensaje
            
def mnsj(mensaje):
    print(mensaje)
    
# Algoritmo principal

dato_numero = dato_n()
mensaje = funcion_datos(dato_numero)
mnsj(mensaje) 