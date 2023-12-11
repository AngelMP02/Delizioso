import tkinter as tk
from tkinter import simpledialog, messagebox
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

        self.ofertas = [
            {"nombre": "Pizza + Bebida 12 euros", "descuento": 0},  # 3x2 en pizzas
            {"nombre": "2 Pizzas + 2 Bebidas 20 euros", "descuento": 0},  # Otra oferta
            {"nombre": "Oferta Especial", "descuento": 10},  # Ejemplo de una oferta con 10% de descuento
        ]

        self.create_widgets()

    def create_widgets(self):
        personalizar_button = tk.Button(self.root, text="Personalizar Pizza", command=self.personalizar_pizza)
        personalizar_button.pack(pady=10)

        pedido_button = tk.Button(self.root, text="Realizar Pedido", command=self.realizar_pedido)
        pedido_button.pack(pady=10)

        ofertas_button = tk.Button(self.root, text="Ofertas", command=self.mostrar_ofertas)
        ofertas_button.pack(pady=10)

    def personalizar_pizza(self):
        ventana_personalizar = tk.Toplevel(self.root)

        tk.Label(ventana_personalizar, text="Seleccione los ingredientes:").pack(pady=10)

        opciones_ingredientes = ["Tomate", "Mozzarella", "Prosciutto", "Aceitunas", "Champiñones"]
        var_ingredientes = {ingrediente: tk.IntVar() for ingrediente in opciones_ingredientes}

        for ingrediente, var in var_ingredientes.items():
            checkbutton = tk.Checkbutton(ventana_personalizar, text=ingrediente, variable=var)
            checkbutton.pack()

        tk.Label(ventana_personalizar, text="Seleccione la bebida:").pack(pady=10)
        opciones_bebida = ["Coca-Cola", "Pepsi", "Agua", "Jugo"]
        var_bebida = tk.StringVar(ventana_personalizar)
        var_bebida.set(opciones_bebida[0])  # Valor predeterminado

        dropdown_bebida = tk.OptionMenu(ventana_personalizar, var_bebida, *opciones_bebida)
        dropdown_bebida.pack()

        add_button = tk.Button(ventana_personalizar, text="Añadir Ingredientes", command=lambda: self.actualizar_ingredientes(var_ingredientes))
        add_button.pack(pady=5)

        confirmar_button = tk.Button(ventana_personalizar, text="Confirmar", command=lambda: self.confirmar_personalizacion(var_ingredientes, var_bebida, ventana_personalizar))
        confirmar_button.pack(pady=10)

    def actualizar_ingredientes(self, var_ingredientes):
        self.ingredientes_seleccionados = [ingrediente for ingrediente, var in var_ingredientes.items() if var.get() == 1]

    def confirmar_personalizacion(self, var_ingredientes, var_bebida, ventana_personalizar):
        ingredientes_personalizados = self.ingredientes_seleccionados or ["Tomate", "Mozzarella"]
        self.builder_delizioso.build_ingredientes_principales_personalizados(ingredientes_personalizados)

        self.builder_delizioso.build_bebida(var_bebida.get())

        precio_pizza = 11  # Precio base de la pizza
        precio_bebida = 2.5  # Precio de la bebida
        precio_total_pizza = precio_pizza + precio_bebida

        oferta_seleccionada = self.mostrar_ofertas()
        if oferta_seleccionada:
            descuento = oferta_seleccionada['descuento']
            precio_con_descuento = self.aplicar_descuentos(precio_total_pizza, descuento)
            self.builder_delizioso.build_precio(precio_con_descuento)
        else:
            self.builder_delizioso.build_precio(precio_total_pizza)

        ventana_personalizar.destroy()

    def realizar_pedido(self):
        self.director.construir_pizza()
        pizza_personalizada = self.builder_delizioso.get_pizza()

        oferta_seleccionada = self.mostrar_ofertas()
        if oferta_seleccionada:
            precio_pizza = 11  # Precio base de la pizza
            precio_bebida = 2.5  # Precio de la bebida
            precio_total_pizza = precio_pizza + precio_bebida
            descuento = oferta_seleccionada['descuento']
            precio_con_descuento = self.aplicar_descuentos(precio_total_pizza, descuento)
            pizza_personalizada.set_precio(precio_con_descuento)
        else:
            pizza_personalizada.set_precio(precio_total_pizza)

        detalles = (
            f"Tipo de masa: {pizza_personalizada.tipo_masa}\n"
            f"Salsa: {pizza_personalizada.salsa}\n"
            f"Ingredientes principales: {', '.join(pizza_personalizada.ingredientes_principales)}\n"
            f"Técnicas de cocción: {pizza_personalizada.tecnicas_coccion}\n"
            f"Presentación: {pizza_personalizada.presentacion}\n"
            f"Maridaje recomendado: {pizza_personalizada.maridaje_recomendado}\n"
            f"Bebida: {pizza_personalizada.bebida}\n"
            f"Precio: ${pizza_personalizada.get_precio()}"
        )
        messagebox.showinfo("Detalles de la pizza personalizada", detalles)

        # Guardar la pizza personalizada en el CSV
        csv_writer = PizzaCSVWriter("pizzas_personalizadas.csv")
        csv_writer.write_pizza_to_csv(pizza_personalizada, pizza_personalizada.get_precio())

    def mostrar_ofertas(self):
        if not self.ofertas:
            messagebox.showinfo("Ofertas", "No hay ofertas disponibles.")
            return

        opciones_ofertas = [oferta['nombre'] for oferta in self.ofertas]
        seleccion = simpledialog.askitemstring("Seleccionar Oferta", "Seleccione la oferta que desea aplicar:", items=opciones_ofertas)

        if seleccion:
            oferta_seleccionada = next((oferta for oferta in self.ofertas if oferta["nombre"] == seleccion), None)
            if oferta_seleccionada:
                messagebox.showinfo("Oferta Seleccionada", f"Ha seleccionado la oferta '{seleccion}'. Descuento: {oferta_seleccionada['descuento']}%")
                return oferta_seleccionada

    def aplicar_descuentos(self, precio_original, descuento_oferta):
        descuento_total = (descuento_oferta / 100) * precio_original
        precio_con_descuento = precio_original - descuento_total
        return precio_con_descuento

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazPedidoPizza(root)
    root.mainloop()
