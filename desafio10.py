# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# (considerando USS1.00 = R$5,06)
if __name__ == '__main__':
    v = float(input('Digite quanto você tem na cateira: '))
    d = v / 5.06
    print('Você pode comprar {:.2f} dólar(s) '.format(d))
