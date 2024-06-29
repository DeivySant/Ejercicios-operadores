#Taller de operadores
nombre = input("Dame tu nombre : ")
print("OK!,", nombre, "Vamos a verificar la siguiente condicion: Si no es cierto que los numeros son mayores que 10" )
print("Dame tus numeros")
a = int(input())
b = int(input())
print("Al verificar la condicion con tus numeros notamos que :", not(a > 10 and b > 10))

