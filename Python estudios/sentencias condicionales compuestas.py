print ("Sistema para calcular el promedio de un alumno.")
nombre = input("Para comenzar, ¿Cual es tu nombre?: ")

matematicas = float (input(nombre + "Ingrese su calificacion en matematicas?: "))
quimica = float (input(nombre + "Ingrese su calificacion en quimica?: "))
biologia = float (input(nombre + "Ingrese su calificacion en biologia?: "))

promedio = (matematicas + quimica + biologia) / 3

if promedio >= 6:
    print ('Felicidades ' + nombre + ' "Aprobaste" ', promedio)
    print ('Felicidades ' + nombre + ' "Aprobaste" ', round (promedio,2))
else:
    print("Lo sentimos" + nombre + "has 'reprobado' con un promedio de: ", promedio)
    print("Lo sentimos" + nombre + "has 'reprobado' con un promedio de: ", round(promedio,1))

print ("Fin")
    
