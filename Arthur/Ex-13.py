#programa para identificar se qual o sexo da pessoa apartir da primeira letra


sexo = input("Qual é o seu genero: \n M - Masculino \n F - Feminino \n O - Outros")

if (sexo == "M"):
    print ("voce é do sexo masculino!")

elif (sexo == "F"):
    print ("Voce é do sexo feminino!")

elif (sexo == "O"):
    print ("voce escolheu outros tipos!")

else:
    print("sexo invalido")