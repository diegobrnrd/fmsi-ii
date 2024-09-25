"""Cálculo do nùmero π (pi)"""


import random as rd


def gerar_dados(n_dados, raio):
    return [rd.uniform(-raio, raio) for _ in range(n_dados)]


def verificacao(lista, raio):
    return lista[0]**2 + lista[1]**2 <= raio**2


def isolada(qtde_simulacoes, qtde_dados, raio):
    contador = sum(verificacao(gerar_dados(qtde_dados, raio), raio) for _ in range(qtde_simulacoes))
    return (contador / qtde_simulacoes) * 4 * raio * raio


def simulacao(qtde_simulacoes, qtde_dados, raio, interacoes):
    total = sum(isolada(qtde_simulacoes, qtde_dados, raio) for _ in range(interacoes))
    return total / interacoes


def principal():
    qtde_dados = 2
    raio = 1
    qtde_simulacoes = 100
    interacoes = 1000
    return simulacao(qtde_simulacoes, qtde_dados, raio, interacoes)


if __name__ == '__main__':
    print(principal())
