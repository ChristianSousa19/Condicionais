import random
import time
itens=("pedra","papel","tesoura")
computador=random.randint(0,2)
print("o computador escolheu {}".format(itens[computador]))
print('''Suas opções
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador=int(input("Qual é a sua jogada?"))
print("o jogador jogou {}".format(itens[jogador]))
if computador==0:
  if jogador==0:
      print("EMPATE")
  elif jogador==2:
    print("JOGADOR VENCE")


if  computador==1:
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print("EMPATE")
    elif jogador==2:
         print("JOGADOR VENCE")

    
elif computador==2:
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print("COMPUTADOR VENCE")
    elif jogador==2:
        print("EMPATE")
   

