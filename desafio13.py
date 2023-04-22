# Faça um algorítimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
if __name__ == '__main__':
    s = float(input('Digite seu salário: '))
    a = s * 0.15
    ns = s + a
    print('seu novo salário agora é: {} '.format(ns))
