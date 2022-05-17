class Producto:
    def __init__(self,nombre,precio,codigo,cantidad):
        self.nombre =nombre
        self.precio=precio 
        self.codigo=codigo
        self.cantidad=cantidad

    def precio_por_producto(self):
        total_por_producto = self.precio*self.cantidad
        return total_por_producto

    def __str__(self):
        return f"{self.nombre},{self.precio},{self.codigo},{self.cantidad}"     





