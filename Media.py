nota=float(input("Digite a primeira nota"))
nota2=float(input("digite sua segunda nota"))
média=(nota+nota2)/2
if 7 > média>=5.0:
    print("\033[0:31mAluno está em recuperação")
elif média<5.0 :
    print("Aluno está reprovado")
elif média>=7:
    print("Aluno aprovado")
