valorc=float(input("Qual é o valor da casa?"))
salario=float(input("Qual é oseu salario?"))
anos=int(input("Em quantos anos você pretende pagar?"))
prestacao=valorc/(anos*12)
minimo=(salario*30)/100
if prestacao<=minimo:
    print("seu emprestimo foi aprovado")
else:
    print("\033[0:31mseu eemprestimo foi negado")
print("aprestação sera de {:.2f}".format(prestacao))