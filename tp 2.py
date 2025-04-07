class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre=nombre
        self.precio=precio
        self.stock=stock

    def obtener_nombre(self):
        return self.nombre
    def obtener_precio(self):
        return self.precio
    def obtener_stock(self):
        return self.stock
    def restar_stock(self):
        x=int(input("ingrese la cantidad que quiera disminuir: "))
        self.stock=self.stock-x
        return self.stock
    def sumar_stock(self):
        c=int(input("ingrese la cantidad que quiera aumentar: "))
        self.stock=self.stock+c
        return self.stock
    
if __name__=="__main__":
    potato=Producto("pera", 4000, 10)
    print(f"Nombre: {potato.obtener_nombre()}")
    print(f"Precio: {potato.obtener_precio()}")
    print(f"Stock: {potato.obtener_stock()}")
    b=str(input("¿quiere aumentar o disminuir?(aumentar=si)(disminuir=no): "))
    if (b=="si"):
        print(f"sumar: {potato.sumar_stock()}")
    else:
        print(f"resto: {potato.restar_stock()}")
