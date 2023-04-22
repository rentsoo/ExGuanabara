# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
if __name__ == '__main__':
    l = float(input('Digíte largura: '))
    a = float(input('Digite altura: '))
    area = l * a
    qtdtinta = area / 2
    print('')
    print('>'*62)
    print('area total de: {}m² e serão necessários {} litros de tinta'.format(area, qtdtinta))
    print('>'*62)
