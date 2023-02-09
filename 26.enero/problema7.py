'''
Nombre: Cristian Perez
Fecha: 29/01/2023
Descripción: patron de numeros
'''


def main():
    
    number = int(input("Digita un numero :"))
    
    #Proceso logico
    unidades = number % 10
    number = number // 10
    decenas = number % 10
    centenas = number //10


    #Condicion


    if (centenas<decenas<unidades):
        print("si")
    else:
        print("no")    

main() # Llamdo a la función principal