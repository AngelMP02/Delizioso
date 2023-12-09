
#Aquí se instancia el PizzaDeliziosoBuilder, se utiliza el DirectorPizza para construir una pizza y se guarda la pizza en un archivo CSV utilizando PizzaCSVWriter.

from pizza_deliciosa_builder import PizzaDeliziosoBuilder
from .director_pizza import DirectorPizza
from csv_writer import PizzaCSVWriter

# Uso del patrón Builder con validación de elecciones
builder_delizioso = PizzaDeliziosoBuilder()
director = DirectorPizza(builder_delizioso)
director.construir_pizza()
pizza_personalizada = builder_delizioso.get_pizza()

print("Detalles de la pizza personalizada:")
print(f"Tipo de masa: {pizza_personalizada.tipo_masa}")
print(f"Salsa: {pizza_personalizada.salsa}")
print(f"Ingredientes principales: {', '.join(pizza_personalizada.ingredientes_principales)}")
print(f"Técnicas de cocción: {pizza_personalizada.tecnicas_coccion}")
print(f"Presentación: {pizza_personalizada.presentacion}")
print(f"Maridaje recomendado: {pizza_personalizada.maridaje_recomendado}")
# Guarda la pizza personalizada en un archivo CSV
csv_writer = PizzaCSVWriter("pizzas_personalizadas.csv")
csv_writer.write_pizza_to_csv(pizza_personalizada)


