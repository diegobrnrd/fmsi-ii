"""Jogando 5 dados, qual a probabilidade da soma dos resultados ser igual a 20?"""


import random as rd


def gerar_dados(n_dados, lados):
    return [rd.randint(1, lados) for _ in range(n_dados)]


def testar_dados(lista, valor):
    return sum(lista) == valor


def simulacao(qtde_simulacoes, qtde_dados, lados, soma):
    contador = sum(testar_dados(gerar_dados(qtde_dados, lados), soma) for _ in range(qtde_simulacoes))
    return contador / qtde_simulacoes


def simulacao_completa(qtde_simulacoes, qtde_dados, lados, soma, interacoes):
    total = sum(simulacao(qtde_simulacoes, qtde_dados, lados, soma) for _ in range(interacoes))
    return total / interacoes


def principal():
    qtde_dados = 5
    lados = 6
    soma = 20
    qtde_simulacoes = 100
    interacoes = 1000
    return simulacao_completa(qtde_simulacoes, qtde_dados, lados, soma, interacoes)


if __name__ == '__main__':
    print(principal())
