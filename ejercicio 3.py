def pedir_numero():
    return int(input("Digite un número: "))


def es_par(num):
    if num % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")


def datos():
    num = 1  

    while num != 0:
        num = pedir_numero()  

        if num != 0:  
            es_par(num)
        else:
            print("Finalizó el programa")


# algoritmo principal
datos()