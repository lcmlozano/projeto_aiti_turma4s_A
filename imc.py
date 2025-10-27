def calcularImc(peso, altura):
    imc = peso / (altura * altura)
    return imc

print(calcularImc(95, 1.80))