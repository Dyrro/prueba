'''
Nombre: Cristian Perez
Fecha: 29/01/2023
Descripción: numero mayor y empate
'''


def main():
    # Asignacion de variables
    number1 = int(input("Digite el pimer numero :"))
    number2 = int(input("Digite el segundo numero :"))
    number3 = int(input("Digite el tercer numero :"))

    # Proceso
    if (number2 < number1 > number3):
        print("El numero mayor es ",number1)
    if (number1 < number2 > number3):
        print("El numero mayor es ",number2)
    if (number1 < number3 > number2):
        print("El numero mayor es ",number3)
            
    else:
        print("hay empate")

main() # Llamdo a la función principal