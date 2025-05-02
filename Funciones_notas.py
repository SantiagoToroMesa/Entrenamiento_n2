#Calculo del promedio de la notas 

def promediolista(list_not):
    if len(list_not) == 0:
        print("No hay notas para calcular el promedio.")
        return None
    promedio = sum(list_not) / len(list_not)
    print(f"El promedio de las notas es {promedio:.2f}")
    return promedio

#Contar las calificaciones mayores a un valor

def contar_mayores(list_not):
    cmayores = 0
    while True:
        try:
            valor = float(input("Ingrese el valor a comparar: "))
            for nota in list_not:
                if nota > valor:
                    print(f"La nota {nota} es mayor que {valor}")
                    cmayores += 1

            if cmayores == 0:
                print(f"No hay notas mayores a {valor}")
                break

            print(f"Hay {cmayores} notas mayores a {valor}")
            break
        except ValueError:
            print("ERROR: Debe ingresar un número válido.")
            continue
        except Exception as e:
            print(f"ERROR: {e}")
            break


def contariguales(list_not):
    cigual = 0
    while True:
        try:
            valor = float(input("Ingrese el valor a comparar: "))
            for nota in list_not:
                if nota == valor:
                    print(f"La nota {nota} es igual a {valor}")
                    cigual += 1

            if cigual == 0:
                print(f"No hay notas iguales a {valor}")
                break

            print(f"Hay {cigual} notas iguales a {valor}")
            break
        except ValueError:
            print("ERROR: Debe ingresar un número válido.")
            continue


def estado(promedio):
    if promedio is None:
        print("No se puede determinar el estado sin promedio. Calcule el promedio de las notas (opción 2) primero.")
        return
    if 60 <= promedio <= 100:
        print("¡Haz aprobado!")
    elif 0 <= promedio < 60:
        print("¡Haz reprobado!")
    else:
        print("Promedio fuera de rango válido.")