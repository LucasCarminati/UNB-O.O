from FigurasGeometricas import Ponto, Circulo, Reta, Retangulo, Triangulo


def workspace():

    # Exemplo de uso da classe Ponto
    ponto1 = Ponto(1, 0, 0)
    print(
        f'Coordenadas do Ponto {ponto1.getNumber()}: ({ponto1.x}, {ponto1.y})')

    # Exemplo de uso da classe Reta
    ponto2 = Ponto(2, 1, 1)
    reta1 = Reta(1, ponto1, ponto2)
    print(
        f'Comprimento da Reta {reta1.nReta}: {reta1.calcularDistancia()} unidades')

    # Exemplo de uso da classe Circulo
    circulo1 = Circulo(1, 2, 2, 3)
    print(
        f'Área do Círculo {circulo1.getNumber()}: {circulo1.calcularArea()} unidades quadradas')
    print(
        f'Perímetro do Círculo {circulo1.getNumber()}: {circulo1.calcularPerimetro()} unidades')

    # Exemplo de uso da classe Retangulo
    ponto3 = Ponto(3, 1, 4)
    ponto4 = Ponto(4, 5, 1)
    retangulo1 = Retangulo(ponto3, ponto4)
    print(
        f'Área do Retângulo {retangulo1.getType()}: {retangulo1.calcularArea()} unidades quadradas')
    print(
        f'Perímetro do Retângulo {retangulo1.getType()}: {retangulo1.calcularPerimetro()} unidades')

    # Exemplo de uso da classe Triangulo
    triangulo1 = Triangulo(1, 0, 0, 3, 0, 0, 4)
    print(
        f'Área do Triângulo {triangulo1.getType()}: {triangulo1.calcularArea()} unidades quadradas')
    print(
        f'Perímetro do Triângulo {triangulo1.getType()}: {triangulo1.calcularPerimetro()} unidades')


if __name__ == "__main__":

    workspace()
