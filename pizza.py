#Define la clase Pizza que representa la estructura básica de una pizza con sus propiedades.
# pizza.py

class Pizza:
    def __init__(self):
        self.tipo_masa = ""
        self.salsa = ""
        self.ingredientes_principales = []
        self.tecnicas_coccion = ""
        self.presentacion = ""
        self.maridaje_recomendado = ""
        self.bebida = ""  # Agregar el atributo de bebida a la clase Pizza
