class Producto:
    def __init__(self, nombre, precio):
        self .nombre = nombre
        self .precio = precio
        self .stock =stock

        def mostrar_info(self) -> None:
            print(f"Producto: {self.nombre}")
            print(f"Precio: ${self.precio}")
            print(f"Stock: {self.stock} unidades")

    def disponible(self) -> bool:
        return self.stock > 0

# Programa principal
laptop1 = Laptop("dell Inspiron",15000, 10)
laptop1.mostrar_info()
print("¿Disponible?:", "Si" if laptop1.disponible() else "No")

#Clase derivada laptop
class Laptop(Producto):
    def __init__(self, nombre, precio, stock, ram, almacenamiento):
        super().__init__(nombre, precio, stock) # reutiliza constructor de Producto
        self._marca = marca
       
    def mostrar_info(self) -> None:
        super().mostrar_info()
        print(f"RAM: {self.ram}") #llama al metodo de la clase base
        print(f"Almacenamiento: {self.almacenamiento}")

        # Programa principal
        if __name__ == "__main__":
            laptop1 = Laptop("Dell Inspiron", 15000, 10, "16GB", "512GB SSD")
            celular1 = Celular("iPhone 13", 20000, 5, "6.1 pulgadas", "12MP")

            print("=== Información de la Laptop ===")
            laptop1.mostrar_info()
            print("¿Disponible?:", "Sí" if laptop1.disponible() else "No")


            print("\n=== Información del Celular ===")
            celular1.mostrar_info()
            print("¿Disponible?:", "Sí" if celular1.disponible() else "No")