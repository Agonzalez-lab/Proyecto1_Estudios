#Conjuncion

print ("Conjuncion (and)")

numero = int(input("Escribe un numero mayor a 2 y menor a 5: "))

if numero > 2 and numero <5:
    print("El numero", numero, " Cumple con al condicion.\n")
else:
    print ("El numero", numero, " NO cumple con la condicion.\n")


#Disyuncion

print ("Disyuncion (or)")

palabra = input("Para cumplir con la condicion escribe 'si' o 'yes':")
    
if palabra == "si" or palabra == "yes":
    print("La condicion se ha cumplido.\n")
else:
    print("La condicion NO se ha cumplido.\n")

#Negacion

print("Negacion (not)")

numero = int(input("Introduce un numero igual a 5: "))

if not numero == 5:
    print("\n El numero es diferente de cinco y SI cumple la condicion.\n")
else:
    print ("\n El numero es igual a cino y NO cumple la condicion.\n")
    


