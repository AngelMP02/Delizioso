from pizza_builder import PizzaBuilder

class DirectorPizza:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def construir_pizza(self):
        self.builder.build_tipo_masa()
        self.builder.build_salsa()
        self.builder.build_ingredientes_principales()
        self.builder.build_tecnicas_coccion()
        self.builder.build_presentacion()
        self.builder.build_maridaje_recomendado()