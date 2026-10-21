import pytest

from src.calculadora import Calculadora


@pytest.fixture
def calculadora():
    return Calculadora()


def test_soma(calculadora):
    assert calculadora.soma(1, 1) == 2


def test_divisao(calculadora):
    calculadora = Calculadora()
    assert calculadora.divisao(1, 1) == 1

def test_positivo(calculadora):
    assert calculadora.positivo(1) is True
    assert calculadora.positivo(-1) is False
    assert calculadora.positivo(0) is True
