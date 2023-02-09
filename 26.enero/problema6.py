'''
Nombre: Cristian Perez
Fecha: 29/01/2023 
Descripción: 3 numeros y su simulitud
'''

def main():
    # Asignacion variables
    number1 = int(input("Digite el primer numero : "))
    number2 = int(input("Digite el segundo numero : "))
    number3 = int(input("Digite el tercer numero : "))

    # Procedimiento 
    if (number1 != number2 ) and (number2 != number3) and (number3 != number1):
        print("0")
    elif(number1 == number2 == number3):
        print("3")
    elif (number1==number2) or (number2==number3) or (number3==number1):
        print("2")
    


main() # Llamdo a la función principal