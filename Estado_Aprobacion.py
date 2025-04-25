#Determinar el estado de aprobacion

def estado():
    try:
        while True:
            nota = int(input("Porfavor ingrese una nota del 0 - 100: "))

            if nota >= 60 and nota <= 100:
                print("¡Haz aprobado!")
                break
        
            elif nota <= 60 and nota >= 0:
                print("¡Haz reprobado!")
                break

            else:
                print("!Debe ingresar un numero entre 0 - 100¡") 

    except ValueError:
        print("ERROR DEBE INGRESAR UN NUMERO")
