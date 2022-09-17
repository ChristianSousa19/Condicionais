import math
numero=int(input("Digite um número inteiro:"))
print('''escolha uma das bases para conversão:
      1 converter para binário
      2 converter para octal
      3 converter para hexadecimal''')
escolha=int(input("digite sua opção:"))
if escolha==1:
    print("o numero {} convertido para binário tem como resultado {}".format(numero,bin(numero)))
if escolha==2:
    print("onumero {} convertido para octal tem como resiultado {}".format(numero,oct(numero)))
if escolha==3:
    print("o numero {} convertido para hexadecimal tem como resultado {}".format(numero,hex(numero)))
else:
    print("Escolha inálida")
