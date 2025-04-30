#Calculo del promedio de la notas 

def promediolista():
    while True:
        try:
            entrada = input("Ingrese las Notas separadas por coma(,): ")
            list_not = [float(nota) for nota in entrada.split(",")]
            for nota in list_not:
                if nota < 0 or nota > 100:
                    print("ERROR: Las notas deben estar entre 0 y 100.")
                    list_not.clear()
                    break
            else:
                promedio = sum(list_not) / len(list_not)
                print(f"El promedio de las notas es {promedio:.2f}")
            # Verificar si la lista de notas no está vacía
        except ValueError:
            print("ERROR: Debe ingresar numeros separados por comas.")
            continue
        return list_not

#Contar las calificaciones mayores a un valor

def contar_mayores(list_not):
    cmayores = 0
    while True:
        valor = int(input("Ingrese el valor a comparar: "))
        for nota in list_not:
            if nota > valor:
                print(f"La nota {nota} es mayor que {valor}")
                cmayores += 1

        if cmayores == 0:
            print(f"No hay notas mayores a {valor}")
            break

        print(f"Hay {cmayores} notas mayores a {valor}")
        break