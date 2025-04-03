class Coche:
    def __init__(self, marca, modelo, añofabricacion):
        self.marca=marca
        self.modelo=modelo
        self.añofabricacion=añofabricacion

    def obtenermarca(self):
        return self.marca
    def obtenermodelo(self):
        return self.modelo
    def obtenerañofabricacion(self):
        return self.añofabricacion
    def años_fabricacion(self):
        años = 2025 - self.añofabricacion
        return años

if __name__ =="__main__":
    coche1=Coche("toyota", "yaris", 1999)

print(f"Marca: {coche1.obtenermarca()}")
print(f"Modelo: {coche1.obtenermodelo()}")
print(f"año de fabricacion: {coche1.obtenerañofabricacion()}")
print(f"años desde fabricacion: {coche1.años_fabricacion()}")

