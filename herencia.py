# miPrimerProyecto.py 🐍

# Clase base Producto: aqui se definen los atributos y métodos comunes a todos los productos
class Producto:
    def __init__(self, nombre, precio, stock):
        self._nombre = nombre
        self._precio = precio
        self._stock = stock

# Método para mostrar la información del producto
    def mostrar_info(self) -> None:
        print(f"Producto: {self._nombre}")
        print(f"Precio: ${self._precio}")
        print(f"Stock: {self._stock} unidades")

    # Método para verificar si el producto está disponible (stock > 0)    

    def disponible(self) -> bool:
        return self._stock > 0


# Clase derivada Laptop:ejemplo de herencia, Laptop es un tipo específico de Producto con atributos adicionales
# Hereda de Producto, por lo que reutiliza su constructor y métodos, además de agregar sus propios atributos y métodos específicos. Esto demuestra el principio de herencia en programación orientada a objetos.
class Laptop(Producto):
    def __init__(self, nombre, precio, stock, ram, almacenamiento):
        super().__init__(nombre, precio, stock)  # reutiliza constructor de Producto
        self._ram = ram
        self._almacenamiento = almacenamiento

    def mostrar_info(self) -> None:
        super().mostrar_info()  
        # Reutilización del codigo con super() para mostrar la información básica del producto, luego se agregan los detalles específicos de la laptop.
        print(f"RAM: {self._ram}")
        print(f"Almacenamiento: {self._almacenamiento}")


# Clase derivada Celular: otro ejemplo de herencia, Celular es otro tipo específico de Producto con atributos adicionales relacionados a las características de un teléfono móvil.
# Hereda de Producto, lo que permite reutilizar el código común y agregar detalles específicos de los celulares, demostrando nuevamente el principio de herencia en programación orientada a objetos.
class Celular(Producto):
    def __init__(self, nombre, precio, stock, pantalla, camara):
        super().__init__(nombre, precio, stock)
        self._pantalla = pantalla
        self._camara = camara

    def mostrar_info(self) -> None:
        super().mostrar_info()
        print(f"Pantalla: {self._pantalla}")
        print(f"Cámara: {self._camara}")


# Programa principal: aquí se crean instancias de Laptop y Celular, se muestra su información y se verifica su disponibilidad. Esto demuestra cómo se pueden utilizar las clases y objetos para organizar y gestionar la información de productos en un programa.
# Se prueban los métodos herados y específicos de cada clase, mostrando cómo la herencia permite reutilizar código y agregar funcionalidades específicas a cada tipo de producto.
if __name__ == "__main__":
    laptop1 = Laptop("Dell Inspiron", 15000, 10, "16GB", "512GB SSD")
    celular1 = Celular("iPhone 13", 20000, 5, "6.1 pulgadas", "12MP")

    print("=== Información de la Laptop ===")
    laptop1.mostrar_info()
    print("¿Disponible?:", "Sí" if laptop1.disponible() else "No")

    print("\n=== Información del Celular ===")
    celular1.mostrar_info()
    print("¿Disponible?:", "Sí" if celular1.disponible() else "No")

