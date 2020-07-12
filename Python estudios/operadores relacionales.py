print ("Introduce dos numero a comparar: \n")

numero = int(input("Introduce el primer numero: "))
numero_dos = int(input("Introduce el segundo numero: "))

print ("\n Los Numero a comparar son: ", numero, " y ", numero_dos, "\n")

if numero == numero_dos:
    print("Es igual..")
if numero != numero_dos:
    print ("Es diferente..")
if numero < numero_dos:
    print ("Es menor..")
if numero > numero_dos:
    print ("Es mayor..")
if numero <= numero_dos:
    print ("Es menor o igual..")
if numero >= numero_dos:
    print ("Es mayor o igual..")

