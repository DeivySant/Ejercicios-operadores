#Taller de operadores logicos
nombre = input("Dame tu nombre : ")
print("OK!,", nombre, "Vamos a verificar la siguiente condicion: si tu primer numero es mayor que 5 y6 si el segundo es menor que 10 o el tercero igual a 20" )
print("Dame tus numeros")
a = int(input())
b = int(input())
c = int(input())
print("Al realizar la verificacion nos damos cuenta que la condicion es ", (a > 5 and b < 10) or c == 20)