#Calculo del promedio de la notas 

def promediolista():
    entrada = input("Ingrese las Notas separadas por coma(,): ")
    list_not = [float(nota) for nota in entrada.split(",")]
    promedio = sum(list_not) / len(list_not)
    print(f"El promedio de las notas es {promedio:.2f}")

#def Not_mayores():
#    while True:
