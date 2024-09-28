salario = float(input("Digite seu salário na empresa: "))
tempoServico = float(input("Digite o seu tempo de serviço na empresa: "))

if tempoServico >= 5:
    print(salario * 0.05 + salario)
elif tempoServico <= 4:
    print(f"Você não tem tempo de serviço requerido para ter o aumento. ")
    print(f"Portanto, seu sálario continuará no valor de {salario}. ")