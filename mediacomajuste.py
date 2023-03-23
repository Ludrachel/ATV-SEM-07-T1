n1 = int(input())
n2 = int(input())
n3 = int(input())
m = (n1 + n2 + n3)/3
def notas():
    if n3 > 8:
        ponto_extra = m +1
        if ponto_extra > 10:
            ponto_extra = 10
            return ponto_extra
        else:
            return ponto_extra
    else:
        return m
print(f'{notas():.2f}')

