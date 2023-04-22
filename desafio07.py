# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
if __name__ == '__main__':
    n1 = float(input('Digite sua primeira nota: '))
    n2 = float(input('Digite sua segunda nota: '))
    m = (n1 + n2) / 2
    print('Sua média é: {:.1f} '.format(m))
