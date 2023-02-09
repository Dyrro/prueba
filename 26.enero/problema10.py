'''
Nombre: Cristian Perez
Fecha: 31/01/2023
Descripción: 
'''


def main():
    alto = int(input("cuantos cuadrados tiene de alto tu barra de chocolate :"))
    Ancho = int(input("cuantos cuadrados tiene de ancho tu barra de chocolate :"))
    requerimiento = int(input("Cuantos cuadros quieres que tenga un trozo de chocolate "))

    if (requerimiento % alto == 0) or (requerimiento % Ancho ==0 ) and (requerimiento <(alto*Ancho)):
        print("si")
    else:
        print("no")

    # Proceso

main()  