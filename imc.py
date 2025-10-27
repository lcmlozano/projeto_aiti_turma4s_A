def calcularImc(peso, altura):
    imc = peso / (altura * altura)
    return imc

def classificarImc(imc):
    if(imc < 18.5):
        print('Abaixo do Peso.')
    else:
        print('peso normal')

imc = calcularImc(95, 1.80)
print(imc)
classificarImc(imc)

