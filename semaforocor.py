def transito(sinal):
    if sinal.upper() == 'V':
        return 'Siga'
    elif sinal.upper() == 'A':
        return 'Atenção'
    elif sinal.upper() == 'E':
        return 'Pare'
def main():
    cor = input()
    print(transito(cor))
if __name__ == '__main__':
    main()
