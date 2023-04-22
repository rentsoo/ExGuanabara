# Faça um algorítimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
if __name__ == '__main__':
    p = float(input('Digite o preço do produto: '))
    d = p * 0.05
    pcd = p - d
    print('Valor com desconto: {:.2f} '.format(pcd))
