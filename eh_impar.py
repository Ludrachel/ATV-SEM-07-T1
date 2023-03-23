def eh_impar(n):
    return n % 2 == 1
def main():
    numero = int(input('digite um número: '))
    resultado = eh_impar(numero)
    if resultado:
        print('True')
    else:
        print('False')
if __name__ == '__main__':
    main()
