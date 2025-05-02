#Calculo del promedio de la notas

def promediolista(list_not):
    if len(list_not) == 0:
        print("No hay notas para calcular el promedio.")
        return None
    #formula para obetener el promedio de las notas
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
                    #contador para las notas mayores al numero ingresado
                    print(f"La nota {nota} es mayor que {valor}")
                    cmayores += 1

            if cmayores == 0:
                #si no hay notas mayores al numero ingresado
                print(f"No hay notas mayores a {valor}")
                break

            #se muestra un resumen de cuantas notas hay mayores al numero ingresado
            print(f"Hay {cmayores} notas mayores a {valor}")
            break
        except ValueError:
            print("ERROR: Debe ingresar un número válido.")
            continue
        except Exception as e:
            print(f"ERROR: {e}")
            break

#contar las calificaciones iguales a un valor

def contariguales(list_not):
    cigual = 0
    while True:
        try:
            valor = float(input("Ingrese el valor a comparar: "))
            for nota in list_not:
                if nota == valor:
                    #contador para las notas iguales al numero ingresado
                    print(f"La nota {nota} es igual a {valor}")
                    cigual += 1

            #si no hay notas mayores al numero ingresado
            if cigual == 0:
                print(f"No hay notas iguales a {valor}")
                break

            #resumen de cuantas notas hay iguales al numero ingresado
            print(f"Hay {cigual} notas iguales a {valor}")
            break
        except ValueError:
            print("ERROR: Debe ingresar un número válido.")
            continue

# Determinar el estado de aprobacion

def estado(promedio):
    if promedio is None:
        print("No se puede determinar el estado sin promedio. Calcule el promedio de las notas (opción 1) primero.")
        return
    # condicional para determinar si aprobo
    if 60 <= promedio <= 100:
        print("¡Haz aprobado!")
    # condicional para determinar si reprobó
    elif 0 <= promedio < 60:
        print("¡Haz reprobado!")
    else:
        print("Promedio fuera de rango válido.")