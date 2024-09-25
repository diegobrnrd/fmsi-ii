def mdc(a, b):
    if a == 0 and b == 0:
        return 'Indeterminado'
    elif b == 0:
        return a
    else:
        return mdc(b, a % b)


if __name__ == '__main__':
    print(mdc(6, 9))
