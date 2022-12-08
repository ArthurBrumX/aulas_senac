#testando if, elif e else

idade = int(input("Digite sua idade: "))
if idade >= 16 and idade < 18: # Caso Verdadeiro
    print ("Pode Votar")
elif idade < 16:
    print ("Apenas estude")
else:
    print ("Pode Dirigir")