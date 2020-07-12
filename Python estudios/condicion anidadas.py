print("Conversor")

print("Menu de opciones:")

print ("Presiona 1 para convertir de numero a palabra")
print ("Presione 2 para convertir de palabra a numero")

opcion = int(input("¿Cual es tu opcion deseada?."))

if opcion == 1:
    print ("Conversor de numero a palabra")

    numero = int(input("¿Cual es el numero que deseas convertir?:"))

    if numero == 1:
        print("El numero es Uno.")
    elif numero == 2:
        print ("El numero es Dos.")
    elif numero == 3:
        print ("El numero es Tres.")
    elif numero == 4:
        print ("El numero es Cuatro.")
    elif numero == 5:
        print ("El numero es Cinco.")
    else:
        print ("Esta permitido hasta el numero cinco!.")
    
elif opcion == 2:
    print ("Conversor de palabra a numero")

    palabra = input("¿Cual es la palabra que deseas convertir a numero?")

    if palabra == "uno":
        print ("El numero es '1'")
    elif palabra == "dos":
        print ("El numero es '2'")
    elif palabra == "tres":
        print ("El numero es '3'")
    elif palabra == "cuatro":
        print ("El numero es '4'")
    elif palabra == "cinco":
        print ("El numero es '5'")
    else:
        print ("Solo esta permitido hasta la palabra cinco")
     
    
else:
    print ("Opcion no disponible")

print("Fin.")
