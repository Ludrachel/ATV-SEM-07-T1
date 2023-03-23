def caractere(x):
    if c.isnumeric():
        return 'número'
    elif x in 'AEIOU':
        return 'vogal'
    elif x in 'BCDFGHJKLMNPQRSTVWXYZ':
        return 'consoante'
    elif x in 'ç/':
        return 'símbolo'
c = input('Digite algo: ').upper()
print(caractere(c))
