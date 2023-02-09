'''
Nombre: Cristian Perez
Fecha: 26/01/2023
Descripción: capacidad monetaria
'''

def main():
    # Asignacion de variables 
    budget = int(input("Cuanto ganas mensualmente? : "))
    food = int(input("Cuanto gastas en comido mensualmente? : "))
    electricity = int(input("Cuantos gastas mensualmente en electricidad? : "))
    wifi = int(input("Cuanto gastas mensualmente por tu internet : "))
    lease = int(input("Cuando es el canon de arrendaminto : "))
    expenses = 0

    # Proceso Logico
    expenses=food+electricity+wifi+lease
    if(budget<expenses):
        print("Salario insuficiente")
    else:
        print("Estas picho plata rey")

main() # Llamdo a la función principal