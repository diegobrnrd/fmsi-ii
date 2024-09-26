"""Probabilidade de doois inteiros serem primos entre si."""

import random as rd


def gerar_dados(maximo):
    return [rd.randint(1, maximo), rd.randint(1, maximo)]


def mdc(a, b):
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return mdc(b, a % b)


def testar_dados(a, b):
    return mdc(a, b) == 1


def simulacao(maximo, quantidade):
    contador = 0
    for i in range(quantidade):
        lista = gerar_dados(maximo)
        if testar_dados(lista[0], lista[1]):
            contador += 1
    return contador / quantidade


def simulacao_completa(maximo, quantidade, simulacoes):
    soma = 0
    for i in range(simulacoes):
        soma += simulacao(maximo, quantidade)
    return soma / simulacoes


def principal():
    maximo = 1000000000000
    quantidade = 1000
    simulacoes = 1000
    return simulacao_completa(maximo, quantidade, simulacoes)


if __name__ == '__main__':
    print(principal())
