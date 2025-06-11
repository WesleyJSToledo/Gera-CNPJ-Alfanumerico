import random
import string

def calcular_dv(cnpj_base):
    pesos_1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos_2 = [6] + pesos_1

    def converter_char(c):
        if c.isdigit():
            return int(c)
        elif c.isalpha():
            return ord(c.upper()) - 48
        else:
            raise ValueError(f"Caractere inválido: {c}")

    def dv(pesos, nums):
        soma = sum([converter_char(n) * p for n, p in zip(nums, pesos)])
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)

    dv1 = dv(pesos_1, cnpj_base)
    dv2 = dv(pesos_2, cnpj_base + dv1)
    return dv1 + dv2

def gerar_cnpj():
    base = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
    cnpj_base = base
    dv = calcular_dv(cnpj_base)
    cnpj = cnpj_base + dv
    return formatar_cnpj(cnpj)

def formatar_cnpj(cnpj):
    return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"


i = int(input("Quantidade de CNPJ: "))
if (i > 0):
    with open('cnpj.txt', 'w') as arquivo:
        for _ in range(i):
            arquivo.write(gerar_cnpj() + '\n')
else:
    print("Insira um número inteiro positivo.")