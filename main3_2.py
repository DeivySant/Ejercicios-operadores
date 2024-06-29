#Taller de operadores logicos
nombre = input("Dame tu nombre : ")
print("OK!,", nombre, "Vamos a verificar si al menos uno de dos numeros son mayores que 10" )
print("Dame tus numeros")
a = int(input())
b = int(input())
print("Hay al menos un numero mayor que 10 ? : ", a > 10 or b > 10)