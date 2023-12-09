from pizza_builder import PizzaBuilder
from pizza import Pizza

class PizzaDeliziosoBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def build_tipo_masa(self):
        self.pizza.tipo_masa = "Masa delgada premium"

    def build_salsa(self):
        # Se agregó la personalización de la salsa
        if hasattr(self, 'salsa_personalizada'):
            self.pizza.salsa = self.salsa_personalizada
        else:
            self.pizza.salsa = "Salsa de autor"

    def build_ingredientes_principales(self):
        # Se agregó la personalización de los ingredientes principales
        if hasattr(self, 'ingredientes_principales_personalizados'):
            self.pizza.ingredientes_principales = self.ingredientes_principales_personalizados
        else:
            self.pizza.ingredientes_principales = ["Tomate", "Mozzarella", "Prosciutto"]

    def build_tecnicas_coccion(self):
        self.pizza.tecnicas_coccion = "Horno tradicional"

    def build_presentacion(self):
        self.pizza.presentacion = "Estilo clásico"

    def build_maridaje_recomendado(self):
        if "Prosciutto" in self.pizza.ingredientes_principales:
            self.pizza.maridaje_recomendado = "Vino tinto"
        else:
            self.pizza.maridaje_recomendado = "Maridaje genérico"

    def build_bebida(self, bebida):
        self.pizza.bebida = bebida  # Método para construir la bebida

    def get_pizza(self):
        return self.pizza

    def build_salsa_personalizada(self, salsa):
        self.salsa_personalizada = salsa

    def build_ingredientes_principales_personalizados(self, ingredientes):
        self.ingredientes_principales_personalizados = ingredientes