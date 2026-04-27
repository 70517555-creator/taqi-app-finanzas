from src.modelo import Finanzas
import pytest


def test_ingreso():
    f=Finanzas()
    f.agregar_ingreso(500)

    assert f.calcular_saldo()==500


def test_gasto():
    f=Finanzas()

    f.agregar_ingreso(1000)
    f.agregar_gasto(300)

    assert f.calcular_saldo()==700


def test_gasto_sin_saldo():
    f=Finanzas()

    with pytest.raises(ValueError):
        f.agregar_gasto(100)
