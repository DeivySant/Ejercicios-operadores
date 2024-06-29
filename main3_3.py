#Taller de operadores logicos
nombre = input("Dame tu nombre : ")
print("OK!,", nombre, "Vamos a verificar si un numero no es mayor que 10" )
print("Dame tu numero")
a = int(input())
print("El numero es mayor que 10 : ", not(a > 10))