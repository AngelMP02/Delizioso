class Menu:
    def __init__(self, codigo, promocion=None):
        self.codigo = codigo
        self.promocion = promocion
        self.elementos = []

    def agregar_elemento(self, elemento):
        self.elementos.append(elemento)

    def calcular_precio_total(self):
        precio_total = sum(elemento.precio for elemento in self.elementos)
        if self.promocion:
            precio_total *= (1 - self.promocion)
        return precio_total
