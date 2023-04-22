# Escreva um programa que leia um valor em metros e o exiba em centímetros e milímetros.
if __name__ == '__main__':
    v = int(input('digite um valor: '))
    c = v * 100
    m = v * 1000
    print('{} centímetros / {} milímetros: '.format(c, m))
