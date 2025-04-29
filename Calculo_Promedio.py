#Calculo del promedio de la notas 

def promediolista():
    while True:
        try:
            entrada = input("Ingrese las Notas separadas por coma(,): ")
            list_not = [float(nota) for nota in entrada.split(",")]
            promedio = sum(list_not) / len(list_not)
            print(f"El promedio de las notas es {promedio:.2f}")
        except ValueError:
            print("ERROR: Debe ingresar solo numeros separados por comas.")
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
        print(f"la cantidad de notas mayores a {valor} es {cmayores}")
        break

