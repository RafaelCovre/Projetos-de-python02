import math
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b **2 - 4 * a * c 

raiz1 = (-b + math.sqrt(delta)) / (2*a)
raiz2 = (-b - math.sqrt(delta)) / (2*a)

print("A primeira raiz é: ", raiz1) 
print("A segunda raiz é: ", raiz2)