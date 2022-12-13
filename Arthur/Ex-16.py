#faça um programa que leia tres numeros e mostre os em ordem decrecente


n1 = float(input("Qual é o primeiro numero: "))

n2 = float(input("Qual é o segundo numero: "))

n3 = float(input("Qual é o terceiro numero: "))

if (n1 > n2) and (n2 > n3):
    print (n3, n2, n1)

elif (n1 > n3) and  (n3 > n2):

# n1>n2 and n2>n3
# n1>n3 and n3>n2

# n2>n1 and n1>n3
# n2>n3 and n3>n1

# n3>n2 and n2>n1
# n3>n1 and n1>n2 

# n1==n2==n3