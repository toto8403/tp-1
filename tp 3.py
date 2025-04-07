class Rectangulo:
    def __init__(self, anchura, longitud):
        self.anchura=anchura
        self.longitud=longitud

    def obtener_anchura(self):
        return self.anchura
    def obtener_longitud(self):
        return self.longitud
    def obtener_perimetro(self):
        P=(self.longitud + self.anchura)*2
        return P
    def obtener_area(self):
        A=self.longitud * self.anchura
        return A
if __name__=="__main__":
    potato=Rectangulo(10, 5)
    print(f"anchura: {potato.obtener_anchura()}")
    print(f"logitud: {potato.obtener_longitud()}")
    print(f"perimetro: {potato.obtener_perimetro()}")
    print(f"area: {potato.obtener_area()}")
