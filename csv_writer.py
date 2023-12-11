#Contiene la clase PizzaCSVWriter que se encarga de escribir detalles de las pizzas en un archivo CSV.
import csv

class PizzaCSVWriter:
    def __init__(self, file_path):
        self.file_path = file_path

    def write_pizza_to_csv(self, pizza):
        with open(self.file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                pizza.tipo_masa,
                pizza.salsa,
                ', '.join(pizza.ingredientes_principales),
                pizza.tecnicas_coccion,
                pizza.presentacion,
                pizza.maridaje_recomendado
            ])
