import math


class Ponto:
    def __init__(self, n, x, y):
        self._n = n
        self.x = x
        self.y = y

    def updateCoord(self, x, y):
        self.x = x
        self.y = y

    def getNumber(self):
        return self._n


class Reta:
    def __init__(self, n, pontoInicial, pontoFinal):
        self.pontoInicial = pontoInicial
        self.pontoFinal = pontoFinal
        self.nReta = n

    def calcularDistancia(self):
        distancia = math.sqrt((self.pontoFinal.x - self.pontoInicial.x)
                              ** 2 + (self.pontoFinal.y - self.pontoInicial.y)**2)
        return distancia

    def getType(self):
        return 'Reta_'

    def updateCoord(self, x1, y1, x2, y2):
        self.pontoInicial.updateCoord(x1, y1)
        self.pontoFinal.updateCoord(x2, y2)

    def printCoord(self):
        print(f'\nA Reta {self.nReta} possui origem em ({self.pontoInicial.x}, {self.pontoInicial.y}) e fim em ({self.pontoFinal.x}, {self.pontoFinal.y}) com distancia de ({self.calcularDistancia()})')


class Circulo(Ponto):
    def __init__(self, n, x, y, raio):
        super().__init__(n, x, y)
        self.raio = raio

    def getType(self):
        return 'Circle_'

    def updateCoord(self, x, y, raio):
        super().updateCoord(x, y)
        self.raio = raio

    def printCoord(self):
        print(f'\nO círculo {self._n} possui origem em: ({self.x}, {self.y})')
        print(f'E o seu raio é {self.raio}')

    def calcularArea(self):
        area = math.pi * self.raio ** 2
        return area

    def calcularPerimetro(self):
        perimetro = 2 * math.pi * self.raio
        return perimetro


class Retangulo:
    def __init__(self, pontoSuperiorEsquerdo, pontoInferiorDireito):
        self.pontoSuperiorEsquerdo = pontoSuperiorEsquerdo
        self.pontoInferiorDireito = pontoInferiorDireito

    def getType(self):
        return 'Retangulo_'

    def calcularArea(self):
        largura = self.pontoInferiorDireito.x - self.pontoSuperiorEsquerdo.x
        altura = self.pontoSuperiorEsquerdo.y - self.pontoInferiorDireito.y
        area = largura * altura
        return area

    def calcularPerimetro(self):
        largura = self.pontoInferiorDireito.x - self.pontoSuperiorEsquerdo.x
        altura = self.pontoSuperiorEsquerdo.y - self.pontoInferiorDireito.y
        perimetro = 2 * (largura + altura)
        return perimetro


class Triangulo(Ponto):
    def __init__(self, n, x1, y1, x2, y2, x3, y3):
        super().__init__(n, x1, y1)
        self.ponto2 = Ponto(n, x2, y2)
        self.ponto3 = Ponto(n, x3, y3)

    def getType(self):
        return 'Triangulo_'

    def calcularLado(self, ponto1, ponto2):
        return math.sqrt((ponto2.x - ponto1.x)**2 + (ponto2.y - ponto1.y)**2)

    def calcularPerimetro(self):
        lado1 = self.calcularLado(self, self.ponto2)
        lado2 = self.calcularLado(self.ponto2, self.ponto3)
        lado3 = self.calcularLado(self.ponto3, self)
        perimetro = lado1 + lado2 + lado3
        return perimetro

    def calcularArea(self):
        lado1 = self.calcularLado(self, self.ponto2)
        lado2 = self.calcularLado(self.ponto2, self.ponto3)
        lado3 = self.calcularLado(self.ponto3, self)
        s = (lado1 + lado2 + lado3) / 2  # Semi-perímetro
        area = math.sqrt(s * (s - lado1) * (s - lado2) * (s - lado3))
        return area
