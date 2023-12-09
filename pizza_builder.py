from abc import ABC, abstractmethod


class PizzaBuilder(ABC):
    @abstractmethod
    def build_tipo_masa(self):
        pass

    @abstractmethod
    def build_salsa(self):
        pass

    @abstractmethod
    def build_ingredientes_principales(self):
        pass

    @abstractmethod
    def build_tecnicas_coccion(self):
        pass

    @abstractmethod
    def build_presentacion(self):
        pass

    @abstractmethod
    def build_maridaje_recomendado(self):
        pass

    @abstractmethod
    def get_pizza(self):
        pass
