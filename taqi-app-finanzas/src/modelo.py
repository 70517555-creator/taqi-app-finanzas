from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Movimiento(Base):
    __tablename__="movimientos"

    id=Column(Integer, primary_key=True)
    tipo=Column(String)
    monto=Column(Float)

engine = create_engine("sqlite:///taqi.db")
Base.metadata.create_all(engine)

Session=sessionmaker(bind=engine)


class Finanzas:
    MAX_GASTOS=3

    def __init__(self):
        self._ingresos=[]
        self._gastos=[]

    def agregar_ingreso(self,monto):
        if monto<0:
            raise ValueError("El monto no puede ser negativo")

        self._ingresos.append(monto)

        session=Session()
        mov=Movimiento(tipo="Ingreso",monto=monto)
        session.add(mov)
        session.commit()
        session.close()


    def agregar_gasto(self,monto):

        if monto<0:
            raise ValueError("Monto inválido")

        if len(self._gastos)>=self.MAX_GASTOS:
            return False

        if monto>self.calcular_saldo():
            raise ValueError("Saldo insuficiente")

        self._gastos.append(monto)

        session=Session()
        mov=Movimiento(tipo="Gasto",monto=monto)
        session.add(mov)
        session.commit()
        session.close()

        return True


    def calcular_saldo(self):
        return sum(self._ingresos)-sum(self._gastos)
