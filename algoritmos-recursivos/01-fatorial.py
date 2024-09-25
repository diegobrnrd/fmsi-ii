def fatorial(n):
    if n < 0:
        return 0
    elif n < 2:
        return n
    else:
        return n * fatorial(n - 1)


if __name__ == '__main__':
    print(fatorial(5))
