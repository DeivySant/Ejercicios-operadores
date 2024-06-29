#Taller de operadores logicos
nombre = input("Dame tu nombre : ")
print("OK!,", nombre, "Vamos a verificar si dos numeros son mayores que 10" )
print("Dame tus numeros")
a = int(input())
b = int(input())
print("Los numeros son mayores que 10 ? : ", a > 10 and b > 10)