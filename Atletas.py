import datetime

Ano=int(input("Qual ano você nasceu"))
idade=2022-Ano
if idade<=9:
    print("Classificação: mirim")
elif idade >9 and idade <=14:
    print("Classificação: Infantil")
elif idade >14 and idade<=19:
    print("Classificação :Junior")
elif idade>19 and idade<25:
    print("classificação :Sênior")
else:
    print("Classificação Master")