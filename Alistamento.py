n=int(input("Em que ano você nasceu?"))
idade=2022-n
print("Quem nasceu em {} tem {} anos em 2022 ".format(n,idade))
if idade==18:
    print("Você deve se alistar")
elif idade<18:
    saldo=idade-18
    print("ainda faltam {} para você se alistar".format(saldo))
elif idade>18:
    saldo2=idade-18
    print("você deveria ter se alistado a {} anos".format(saldo2))