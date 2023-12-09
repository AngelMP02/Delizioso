import tkinter as tk
from tkinter import messagebox
from pizza_deliciosa_builder import PizzaDeliziosoBuilder
from director_pizza import DirectorPizza
from csv_writer import PizzaCSVWriter

class InterfazPedidoPizza:
    def __init__(self, root):
        self.root = root
        self.root.title("Personalizar Pizza")

        self.builder_delizioso = PizzaDeliziosoBuilder()
        self.director = DirectorPizza(self.builder_delizioso)

        self.ingredientes_seleccionados = []
        self.salsa_seleccionada = ""
        self.bebida_seleccionada = ""

        self.create_widgets()

    def create_widgets(self):
        # Botón para personalizar la pizza
        personalizar_button = tk.Button(self.root, text="Personalizar Pizza", command=self.personalizar_pizza)
        personalizar_button.pack(pady=10)

        # Botón para realizar el pedido y guardar en CSV
        pedido_button = tk.Button(self.root, text="Realizar Pedido", command=self.realizar_pedido)
        pedido_button.pack(pady=10)

    def personalizar_pizza(self):
        # Abrir una nueva ventana para personalizar la pizza
        ventana_personalizar = tk.Toplevel(self.root)

        # Etiqueta y checkbuttons para ingredientes
        tk.Label(ventana_personalizar, text="Seleccione los ingredientes:").pack(pady=10)

        opciones_ingredientes = ["Tomate", "Mozzarella", "Prosciutto", "Aceitunas", "Champiñones"]
        var_ingredientes = {ingrediente: tk.IntVar() for ingrediente in opciones_ingredientes}

        for ingrediente, var in var_ingredientes.items():
            checkbutton = tk.Checkbutton(ventana_personalizar, text=ingrediente, variable=var)
            checkbutton.pack()

        
        # Dropdown para seleccionar la bebida
        tk.Label(ventana_personalizar, text="Seleccione la bebida:").pack(pady=10)
        opciones_bebida = ["Coca-Cola", "Pepsi", "Agua", "Jugo"]
        var_bebida = tk.StringVar(ventana_personalizar)
        var_bebida.set(opciones_bebida[0])  # Valor predeterminado

        dropdown_bebida = tk.OptionMenu(ventana_personalizar, var_bebida, *opciones_bebida)
        dropdown_bebida.pack()

        # Agregar botones para añadir/quitar ingredientes y confirmar la selección
        add_button = tk.Button(ventana_personalizar, text="Añadir Ingredientes", command=lambda: self.actualizar_ingredientes(var_ingredientes))
        add_button.pack(pady=5)

        confirmar_button = tk.Button(ventana_personalizar, text="Confirmar", command=lambda: self.confirmar_personalizacion(var_ingredientes, var_bebida, ventana_personalizar))
        confirmar_button.pack(pady=10)

    def actualizar_ingredientes(self, var_ingredientes):
        # Actualizar la lista de ingredientes seleccionados
        self.ingredientes_seleccionados = [ingrediente for ingrediente, var in var_ingredientes.items() if var.get() == 1]

    def confirmar_personalizacion(self, var_ingredientes, var_bebida, ventana_personalizar):
        # Aplicar la personalización a la pizza
        ingredientes_personalizados = self.ingredientes_seleccionados or ["Tomate", "Mozzarella"]  # Ingredientes predeterminados si no se selecciona ninguno
        self.builder_delizioso.build_ingredientes_principales_personalizados(ingredientes_personalizados)

        # Aplicar la elección de  bebida
       
        self.builder_delizioso.build_bebida(var_bebida.get())

        # Cerrar la ventana de personalización
        ventana_personalizar.destroy()

    def realizar_pedido(self):
        # Construir la pizza utilizando el DirectorPizza
        self.director.construir_pizza()
        pizza_personalizada = self.builder_delizioso.get_pizza()

        # Mostrar detalles de la pizza personalizada
        detalles = (
            f"Tipo de masa: {pizza_personalizada.tipo_masa}\n"
            f"Salsa: {pizza_personalizada.salsa}\n"
            f"Ingredientes principales: {', '.join(pizza_personalizada.ingredientes_principales)}\n"
            f"Técnicas de cocción: {pizza_personalizada.tecnicas_coccion}\n"
            f"Presentación: {pizza_personalizada.presentacion}\n"
            f"Maridaje recomendado: {pizza_personalizada.maridaje_recomendado}\n"
            f"Bebida: {pizza_personalizada.bebida}"
        )
        messagebox.showinfo("Detalles de la pizza personalizada", detalles)

        # Guardar la pizza personalizada en un archivo CSV
        csv_writer = PizzaCSVWriter("pizzas_personalizadas.csv")
        csv_writer.write_pizza_to_csv(pizza_personalizada)

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazPedidoPizza(root)
    root.mainloop()