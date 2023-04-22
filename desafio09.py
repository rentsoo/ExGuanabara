# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
if __name__ == '__main__':
    n = int(input('Digite um número: '))
    for c in range (1, 11):
        t = n * c
        print('{} X {} = {} '.format(n, c, t))
