# crie um algorítimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
if __name__ == '__main__':
    n = float(input(('Digite um número: ')))
    d = n * 2
    t = n * 3
    r = n **(1/2)
    print('O dobro é: {}, o triplo é: {} e a raiz é: {} '.format(d, t, r))
