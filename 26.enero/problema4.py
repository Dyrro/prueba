'''
Nombre: Cristian Perez
Fecha: 26/01/2023
Descripción: Divisible
'''


def main():
    # Asignacion de variables
    number = int(input("Digita un numero : "))

    # Proceso Logico 
    if (number%10==0):
        print(f"El numero {number} es divisibles por 10")
    else:
        print(f"El numero {number} no es divisible por 10")

main() # Llamdo a la función principal