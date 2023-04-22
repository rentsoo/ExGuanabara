# Crie um algorítimo que leia um número inteiro e mostre na tela o seu antecessor e seu sucessor.
if __name__ == '__main__':
    n = int(input('Digite um número: '))
    an = n - 1
    su = n + 1
    print('O número que você digitou é: {}, o seu antecessor é: {} e o seu sucessor é: {} '.format(n, an, su))
