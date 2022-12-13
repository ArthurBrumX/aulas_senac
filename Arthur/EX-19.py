""" 12 - Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês. Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220."""


nome = (input("Qual é o seu nome: ")) # perunta ao usuario qual é o seu nome
horas_trab = float(input("Qual o valor das suas horas: ")) # Pergunta ao usuario qual o valor da sua hora trabalhada
horas = float(input("Quantas horas trabalhadas: ")) # Pergunta ao usuario quantas horas ele trabalhou
salario = horas * horas_trab # atribuindo a variavel (salario) suas o valor da sua hora trabalhada (horas) vezes (*) a quantidade de suas horas trabalhadas (horas_trab)
fgts = salario * 11 / 100 # atraves da tabela, atribuindo o valor do seu FGTS de acordo com a conta (fgts) (= -> recebe) (o valor de -> salario) (* -> vezes) (11%) (/ - dividido) por 100
inss = salario * 10 / 100 # atraves da tabela, atribuindo o valor do seu INSS de acordo com a conta (INSS) (= -> recebe) (o valor de -> salario) (* -> vezes) (10%) (/ - dividido) por 100

if (salario <= 900): # se caso o salario dele for de 900 ou menos, sera impromido a seguinte mensagem
    print("isento do imposto de renda - FGTS") # caso o salario dele for igual ou menor que 900 R$ sera imprimido na tela a seguinte mensagem
    percento = 0  #imposto de renda
    novo_salario = salario - percento - inss
    print ("seu FGTS será de: ", fgts)
    print ("Seu INSS será de: ", inss)
    print ("O seu salario bruto é de: ", salario)
    print ("Seu novo salario será de: ", novo_salario)
    print ("o seu imposto de renda será de: ", percento) # Valor do imposto de renda

elif (salario <= 1500):
    percento = salario * 5 / 100 #imposto de renda
    novo_salario = salario - percento - inss
    print ("seu FGTS será de: ", fgts)
    print ("Seu INSS será de: ", inss)
    print ("O seu salario bruto é de: ", salario)
    print ("Seu novo salario será de: ", novo_salario)
    print ("o seu imposto de renda será de: ", percento) # Valor do imposto de renda
    
    

elif (salario <= 2500):
    percento = salario * 10 / 100 #imposto de renda
    novo_salario = salario - percento - inss
    print ("Seu FGTS será de: ", fgts)
    print ("Seu INSS será de: ", inss)
    print ("seu salario bruto é de: ", salario)
    print ("Seu salario será de: ", novo_salario)
    print ("o seu imposto de renda será de: ", percento) # Valor do imposto de renda

elif (salario >= 2501):
    percento = salario * 20 / 100 #imposto de renda
    novo_salario = salario - percento - inss
    print ("Seu FGTS será de: ", fgts) #o valor do FGTS
    print ("Seu INSS será de : ",inss)# o valor do INSS
    print ("Seu salario bruto será de: ",salario) #salario bruto sem o desconto do inss e do fgts
    print ("Seu salario será de: ", novo_salario) # salario liquido com os descontos
    print ("o seu imposto de renda será de: ", percento) # Valor do imposto de renda
    