from producto import Producto
from listaproductos import lista_productos

def total(lista_productos):
    v=0
    for i in range(len(lista_productos)):
        v= v + lista_productos[i].precio_por_producto()
    return v


class Factura:
    __tasa = 16
    def __init__(self,total):
        self.total = total

    def pagar(self):
        tasa_total = self.total*self.__tasa/100
        return tasa_total + self.total

if __name__ == '__main__': 
    factura1= Factura(total(lista_productos))
    print(factura1.pagar())


