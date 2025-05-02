from Funciones_notas import promediolista, contar_mayores, contariguales, estado

# menu de opciones para el usuario final
def menu():
    print("""\nBienvenido al sistema de gestion de calificaciones y estadisticas
=================================================================
        \nMenu de opciones:\n 
            1. Calcular el promedio
            2. Determinar el estado de aprobacion
            3. Contar calificaciones mayores
            4. Verificar y contar calificaciones especificas
            5. Volver a ingresar las notas
            6. Salir
        """)

    opcion = input("Selecione una opcion: ")
    return opcion

# Validar la entrada de notas

def listanotas():
    while True:
        try:
            print("="* 65 + "\n")
            entrada = input("Ingrese las Notas separadas por coma(,): ")
            list_not = [float(nota) for nota in entrada.split(",")]
            # Validar que todas las notas estén en el rango 0-100
            if all(0 <= nota <= 100 for nota in list_not):
                return list_not
            else:
                print("ERROR: Las notas deben estar entre 0 y 100.")
        except ValueError:
            print("ERROR: Debe ingresar números separados por comas.")

lista = listanotas()
prom = None


while True:

# Se muestra el menu de opciones
    opcion = menu()

    if opcion == "1":
        # Se calcula el promedio
        prom = promediolista(lista)


    elif opcion == "2":
        # Se determina el estado de aprobacion
        estado(prom)


    elif opcion == "3":
        # Se cuentan las calificaciones mayores a un numero ingresado por el usuario
        contar_mayores(lista)

    elif opcion == "4":
        # Se cuentan las calificaciones iguales a un numero ingresado por el usuario
        contariguales(lista)

    elif opcion == "5":
        # Se vuelve a ingresar las notas
        lista.clear()
        prom = None
        lista = listanotas()

    # Se verifica si el usuario quiere salir del program
    elif opcion == "6":
        # Se sale del programa
        print("Saliendo del programa...")
        break

    else: 
        print("Debes ingresar un numero del 1 al 6")