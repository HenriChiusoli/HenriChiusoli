numero = []
soma = 0
print("Digite 5 números.")
for i in range(5):
    numeros = float(input("Digite o número: "))
    numero.append(numeros)
    soma += numeros
print(soma)