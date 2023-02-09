""" Nombre: Cristian Perez
Fecha: 08/02/2023
Descripción:   """



def main():
    # Asignacion de variables
    #esta parte del codigo me busca la diferencia entre el patron (1,10,2,9,3,8......)
    number = int(input("Digite un numero :"))
    muestra = 0
    result = 0
    dif = 1
    cont = 1
    cont2 = 2
    

    if (number%2==0):
        while (cont<=number/2):
            muestra = number - dif
            dif += 2
            cont += 1
            while (cont2<=10):
                #result=muestra-number
                result=number - result
                number -=1
                cont2 +=1
                print(result)
            

        

    """ number = int(input("Digite un numero :"))
    muestra = 0
    dif = 1
    cont = 1
    resul = 0
    cont2 = 1

    if (number%2==0):
        while (cont<number/2):
            muestra = number - dif
            dif += 2
            cont += 1
            while(cont2<number/10):
                number -=1
                resul = number-muestra
                cont2 +=1
                print(resul) """
    


            

    
    """ avr = number-9
    result= number-avr
    print(result) """

    # Proceso logico
   

main()