class Calculadora:
    def soma(self, a, b):
        return a + b

    def divisao(self, a, b):
        return a / b

    def potencia(self, a, b):
        return a**b

    def raiz_quadrada(self, a: float) -> float:
        if not isinstance(a, (int, float)):
            raise TypeError("Numero deve ser um float")
        if a < 0:
            raise ValueError("Numero deve ser positivo")
        return a**0.5

    def positivo(self, a: float) -> bool:
        if not isinstance(a, (int, float)):
            raise TypeError("Numero deve ser um float")
        return a > 0