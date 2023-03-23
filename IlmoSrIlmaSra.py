def naturalidade(sexo,nome):
    if sexo == 1:
        return f'Ilmo Sr. {nome}'
    elif sexo == 2:
        return f'Ilma Sra. {nome}'
def main():
    n = input('digite seu nome: ')
    s = int(input('digite 1 se seu sexo for masculino, ou 2 se for feminino : '))
    print(naturalidade(s,n))
if __name__ == '__main__':
    main()
