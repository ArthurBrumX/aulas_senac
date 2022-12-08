#Receber o salario atual de um funcionario, calcule o valor do novo salario reajustado de acordo com a tabela

salario = float(input("Qual é o seu salario: "))

if (salario < 500):
    reajuste = salario + salario * 15 / 100
    print("seu salario é de: ", salario, "e teve o reajuste de ", reajuste)

elif (salario >= 500) or (salario <= 1000):
    reajuste = salario + salario * 10 / 100 
    print ("seu salario é de: ",salario, "e teve o reajuste de ", reajuste)

else:
    reajuste = salario + salario * 5 / 100
    print ("seu salario é de: ",salario, "e teve o reajuste de ", reajuste)

# o numero dividido por 100 vc consegue acha a porcentagem











