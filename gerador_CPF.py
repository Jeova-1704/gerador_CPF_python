import random

linha = '\033[1;31m=\033[m'
nome = 'Gerador de CPF válido'

print(linha * (len(nome) + 6))
print(nome.center((len(nome) + 6)))
print(linha * (len(nome) + 6))

n = int(input('Quantos CPFs você deseja gerar: '))

print(linha * (len(nome) + 6))
for _ in range(n):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

    soma_digitos = 0
    contador = 10

    for num in nove_digitos:
        soma_digitos += int(num) * contador
        contador -= 1

    resto_divisao = soma_digitos % 11

    if resto_divisao < 2:
        penultimo_digito = 0

    else:
        penultimo_digito = 11 - resto_divisao

    #codigo de verificação do segundo digito

    dez_digitos = nove_digitos + str(penultimo_digito)
    contador_2 = 11
    soma_digitos_2 = 0

    for num in dez_digitos:
        soma_digitos_2 += int(num) * contador_2
        contador_2 -= 1

    resto_divisao_2 = soma_digitos_2 % 11

    if resto_divisao_2 < 2 :
        ultimo_digito = 0
    else:
        ultimo_digito = 11 - resto_divisao_2

    cpf_final = nove_digitos[:3] + '.' + nove_digitos[3:6] + '.' + nove_digitos[6:] + '-' + str(penultimo_digito) + str(ultimo_digito)

    print(cpf_final)

print(linha * (len(nome) + 6))
