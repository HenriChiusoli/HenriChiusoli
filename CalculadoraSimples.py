NumeroUm = float(input("Digite um número: "))
NumeroDois = float(input("Digite um número: "))
Operacao = input("Digite a operação desejada: ")

resultadoSoma = NumeroUm + NumeroDois
resultadoSubtracao = NumeroUm - NumeroDois
resultadoDivisao = NumeroUm / NumeroDois
resultadoMultiplicacao = NumeroUm * NumeroDois

if Operacao == "Soma":
    print(resultadoSoma)
elif Operacao == "Subtracao":
    print(resultadoSubtracao)
elif Operacao == "Divisao":
    print(resultadoDivisao)
elif Operacao == "Multiplicacao":
    print(resultadoDivisao)
