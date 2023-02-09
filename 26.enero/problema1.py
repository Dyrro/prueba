'''
Nombre: Cristian Perez
Fecha: 26/01/2023
Descripción: naruralesco
'''

# Definición de la función principal o main()
def main():
    #Asignacion de variables
    sound = int(input("Digite el número de sonidos emitidos por minuto por el grillo :"))
    temperature = 0
    
    #Proceso Logico

    if (sound>=0): 
        temperature = (sound/4)+40
        print("La temperatura actual es de",temperature)
    else:
        print("Digitaste un numero negativo, porfavor cuenta los sonidos emitidos del grillo")


main() # Llamdo a la función principal
