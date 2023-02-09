
""" Nombre: Cristian Perez
Fecha: 07/02/2023
Descripción:  """



def main():
    # Asignacion de variables
    number = int(input("Digite un numero para calcular su factorial: "))
    factorial = 1
    cont = 1

    # Proceso logico
    while (cont<=number) :   
        factorial = factorial*cont
        cont += 1
    print(factorial) 

main()  