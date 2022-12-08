# programa para realizar a leitura de duas notas de um alino e calcular a media entre eles e dizer se ele soi aprovado ou nao

nota1 = float(input("qual é a primeira nota: "))

nota2 = float(input("qual é a segunda nota "))

media = (nota1 + nota2) / 2

if (media >= 7 and media < 10):
    print ("Aluno Aprovado!")

elif (media < 7):
    print("aluno Reprovado!")

elif (media == 10):
    print("Aluno Aprovado com Distinção")
