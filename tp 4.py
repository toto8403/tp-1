class Circulo:
    def __init__(self, radio, diametro):
        self.radio=radio
        self.diametro=diametro

    def obtener_radio(self):
        return self.radio
    def obtener_diametro(self):
        return self.diametro
    def obtener_circunferencia(self):
        C=self.diametro*3.14
        return C
    def obtener_area(self):
        A=(self.radio+3.14)*2
        return A
if __name__=="__main__":
    potato=Circulo(10, 10)
    print(f"radio: {potato.obtener_radio()}")
    print(f"diametro: {potato.obtener_diametro()}")
    print(f"circunferencia: {potato.obtener_circunferencia()}")
    print(f"area: {potato.obtener_area()}")
