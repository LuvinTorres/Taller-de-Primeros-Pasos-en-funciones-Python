# funciones

def menu():
    print("digite la letra 'A' para Actualizar el sistema")
    print("digite la letra 'E' para Eliminar el catalogo")
    print("digite la letra 'C' para Crear productos")
    print("digite la letra 'S' para Salir del programa")
    
def procesar_opcion(letra):
    if letra == 'A' or letra == 'a':
        print("Actualizando sistema...\n")
    elif letra == 'E' or letra == 'e':
        print("Eliminando catálogo...\n")
    elif letra == 'C' or letra == 'c':
        print("Creando productos...\n")
    elif letra == 'S' or letra == 's':
        print("Finalizó con éxito.\n")
        return False  
    else:
        print("Opción no válida. Intente de nuevo.\n")
    return True      
   
def proceso():
    while True:
      menu()
      letra = input("Digite una opcion:")
      if not procesar_opcion(letra):
       break
      
      print("el DO-While ha finalizado.\n")
      
      
# algoritmo principal
      
proceso()
      
