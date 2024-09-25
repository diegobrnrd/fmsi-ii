def exponencial_modular(a, n, m):
    if m <= 1:
        return 'Impossível calcular'
    if a == 0 and n == 0:
        return 'Impossível calcular'
    if n == 0:
        return 1
    if n % 2 == 0:
        metade = exponencial_modular(a, n // 2, m)
        return (metade * metade) % m
    else:
        return (a * exponencial_modular(a, n - 1, m)) % m


if __name__ == '__main__':
    print(exponencial_modular(3, 4, 10))
