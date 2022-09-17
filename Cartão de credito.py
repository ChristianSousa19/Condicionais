preçonormal=float(input("Digite o valor do produto:"))
print('''formas de pagamento
[1]a vista dinhero/cheque
[2] a vista cartão
[3] 2x no cartão
[4] 3x no cartão''')
escolha=int(input("Selecione sua opção"))
dc=preçonormal- (preçonormal*10/100)
vc=preçonormal-(preçonormal*5/100)
x2=preçonormal
x3=preçonormal+(preçonormal*20/100)
if escolha==1:
    print("você devera pagar {} R$".format(dc))
elif escolha==2:
    print("voce devera pagar {} R$".format(vc))
elif escolha==3:
    parcela = preçonormal / 2
    print("Você devera pagar {} R$".format(parcela))
elif escolha==4:
    total=int(input("Quantas parcelas :"))
    parcela1=total/x3
    print("Sua comra será parcelada em {} vezes e custará {} R$".format(total,x3))
else:
    print("\033[0:31mopção inválida")