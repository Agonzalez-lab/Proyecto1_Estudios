#Programa que determine si un numero es par o impar

print("* Programa que determina si un numero es par o impar *")

numero = int(input("Escriba un numero entero: "))

if numero % 2 == 0:
    print ("El numero ", numero, "es par.")
elif numero % 2 == 1:
    print ("El numero", numero, "es impar.")


