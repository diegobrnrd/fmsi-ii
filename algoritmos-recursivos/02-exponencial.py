def exponencial(a, n):
    if a == 0 and n == 0:
        return 'Impossível calcular.'
    elif n == 0:
        return 1
    elif n % 2 == 0:
        metade = exponencial(a, n // 2)
        return metade * metade
    else:
        return a * exponencial(a, n - 1)

if __name__ == '__main__':
    print(exponencial(5, 2))
