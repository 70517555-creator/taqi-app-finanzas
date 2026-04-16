class Finanzas:
    MAX_GASTOS = 3

    def __init__(self):
        self._ingresos = []
        self._gastos = []

    def agregar_ingreso(self, monto):
        if monto < 0:
            raise ValueError("El monto no puede ser negativo")
        self._ingresos.append(monto)

    def agregar_gasto(self, monto):
        if monto < 0:
            raise ValueError("El monto no puede ser negativo")

        if len(self._gastos) >= self.MAX_GASTOS:
            return False

        if monto > self.calcular_saldo():
            raise ValueError(
                f"No tienes saldo suficiente. Disponible: S/ {self.calcular_saldo():.2f}"
            )

        self._gastos.append(monto)
        return True

    def calcular_saldo(self):
        return sum(self._ingresos) - sum(self._gastos)