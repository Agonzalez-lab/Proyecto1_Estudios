
print ("* Vacaciones con rappi *")

nombre_empleado = input("Escriba el nombre del empleado: ")
clave_departamento = int(input ("Escriba la clave en donde esta asignado el empleado:"))
antiguedad_empleado = float(input("Escriba los años que lleva de empleado en rappi: "))

if clave_departamento == 1:
                         
    if antiguedad_empleado == 1 and atiguedad_empleado < 2:
        print("El empleado", nombre_empelado, "tiene derecho a 6 dias de vacaciones.")
    elif antiguedad_empleado >= 2 and antiguedad_empleado <= 6:
        print("El empleado", nombre_empleado, "tiene derecho a 14 dias de vacaciones.")
    elif antiguedad_empleado >= 7:
        print("El empleado", nombre_empleado, "tiene derecho a 20 dias de vacaciones.")
    else:
        print("El empleado", nombre_empleado, "aun no tiene derecho a vacaciones.")
        
elif clave_departamento == 2:
    
    if antiguedad_empleado == 1 and atiguedad_empleado < 2:
        print("El empleado", nombre_empelado, "tiene derecho a 7 dias de vacaciones.")
    elif antiguedad_empleado >= 2 and antiguedad_empleado <= 6:
        print("El empleado", nombre_empleado, "tiene derecho a 15 dias de vacaciones.")
    elif antiguedad_empleado >= 7:
        print("El empleado", nombre_empleado, "tiene derecho a 22 dias de vacaciones.")
    else:
        print("El empleado", nombre_empleado, "aun no tiene derecho a vacaciones.")

elif clave_departamento == 3:
    if antiguedad_empleado == 1 and atiguedad_empleado < 2:
        print("El empleado", nombre_empleado, "tiene derecho a 10 dias de vacaciones.")
    elif antiguedad_empleado >= 2 and antiguedad_empleado <= 6:
        print("El empleado", nombre_empleado, "tiene derecho a 20 dias de vacaciones.")
    elif antiguedad_empleado >= 7:
        print("El empleado", nombre_empleado, "tiene derecho a 30 dias de vacaciones.")
    else:
        print("El empleado", nombre_empleado, "aun no tiene derecho a vacaciones.")

else:
    print("La clave digitada no existe vuelve a intentarlo.")
    
