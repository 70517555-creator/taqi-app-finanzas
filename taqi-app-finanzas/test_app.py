import pytest
from modelo import Finanzas

def test_ingreso_valido():
    f=Finanzas()
    f.agregar_ingreso(500)

    assert f.calcular_saldo()==500


def test_ingreso_negativo():
    f=Finanzas()

    with pytest.raises(ValueError):
        f.agregar_ingreso(-50)


def test_gasto_valido():
    f=Finanzas()

    f.agregar_ingreso(1000)
    f.agregar_gasto(300)

    assert f.calcular_saldo()==700


def test_gasto_supera_saldo():
    f=Finanzas()

    f.agregar_ingreso(100)

    with pytest.raises(ValueError):
        f.agregar_gasto(500)


def test_max_gastos():
    f=Finanzas()

    f.agregar_ingreso(1000)

    f.agregar_gasto(100)
    f.agregar_gasto(100)
    f.agregar_gasto(100)

    assert f.agregar_gasto(50)==False
