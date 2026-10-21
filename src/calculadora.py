import bcrypt


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

    def media(self, lista: list[float]) -> float:
        if not isinstance(lista, list):
            raise TypeError("Lista deve ser uma lista")
        if not lista:
            raise ValueError("Lista não pode ser vazia")
        return sum(lista) / len(lista)

    def soma_lista(self, lista: list[float]) -> float:
        if not isinstance(lista, list):
            raise TypeError("Lista deve ser uma lista")
        if not lista:
            raise ValueError("Lista não pode ser vazia")
        return sum(lista)

    def criptografa(self, data: str) -> str:
        if not isinstance(data, str):
            raise TypeError("Data deve ser uma string")
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(data.encode(), salt)
        return hashed.decode()
        