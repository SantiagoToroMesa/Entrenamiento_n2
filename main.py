from Estado_Aprobacion import estado
from Calculo_Promedio import promediolista

def menu():
    print("""\nBienvenido al sistema de gestion de calificaciones y estadisticas
=================================================================
        \nMenu de opciones:\n 
            1. Determinar el estado de aprobacion
            2. Calcular el promedio
            3. Contar calificaciones mayores
            4. Verificar y contar calificaciones especificas
            5. Salir
        """)
    
    opcion = input("Selecione una opcion: ")
    return opcion

while True:
    opcion = menu()

    if opcion == "1":
        estado()

    elif opcion == "2":
        promediolista()

    #elif opcion == "3":

    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else: 
        print("Debes ingresar un numero del 1 al 5")