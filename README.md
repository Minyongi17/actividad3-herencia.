# Actividad Formativa 3 - Herencia en Python

Este proyecto corresponde a la Actividad Formativa 3 de la materia de Programación Orientada a Objetos 
El objetivo es aplicar **herencia** y **reutilización de código** en Python.

## 📌 Conceptos aplicados
- **Herencia:** Clases `Laptop` y `Celular` derivadas de la clase base `Producto`.
- **Reutilización de código:** Uso de `super().__init__()` y `super().mostrar_info()` para aprovechar atributos y métodos de la clase base.
- **Sobrescritura de métodos:** Extensión del método `mostrar_info()` en las subclases para mostrar atributos propios.

## 📑 Código principal (`herencia.py`)
```python
class Producto:
    def __init__(self, nombre, precio, stock):
        self._nombre = nombre
        self._precio = precio
        self._stock = stock

    def mostrar_info(self) -> None:
        print(f"Producto: {self._nombre}")
        print(f"Precio: ${self._precio}")
        print(f"Stock: {self._stock} unidades")

    def disponible(self) -> bool:
        return self._stock > 0


class Laptop(Producto):
    def __init__(self, nombre, precio, stock, ram, almacenamiento):
        super().__init__(nombre, precio, stock)
        self._ram = ram
        self._almacenamiento = almacenamiento

    def mostrar_info(self) -> None:
        super().mostrar_info()
        print(f"RAM: {self._ram}")
        print(f"Almacenamiento: {self._almacenamiento}")


class Celular(Producto):
    def __init__(self, nombre, precio, stock, pantalla, camara):
        super().__init__(nombre, precio, stock)
        self._pantalla = pantalla
        self._camara = camara

    def mostrar_info(self) -> None:
        super().mostrar_info()
        print(f"Pantalla: {self._pantalla}")
        print(f"Cámara: {self._camara}")


if __name__ == "__main__":
    laptop1 = Laptop("Dell Inspiron", 15000, 10, "16GB", "512GB SSD")
    celular1 = Celular("iPhone 13", 20000, 5, "6.1 pulgadas", "12MP")

    print("=== Información de la Laptop ===")
    laptop1.mostrar_info()
    print("¿Disponible?:", "Sí" if laptop1.disponible() else "No")

    print("\n=== Información del Celular ===")
    celular1.mostrar_info()
    print("¿Disponible?:", "Sí" if celular1.disponible() else "No")




#Ejemplo de salida 

=== Información de la Laptop ===
Producto: Dell Inspiron
Precio: $15000
Stock: 10 unidades
RAM: 16GB
Almacenamiento: 512GB SSD
¿Disponible?: Sí

=== Información del Celular ===
Producto: iPhone 13
Precio: $20000
Stock: 5 unidades
Pantalla: 6.1 pulgadas
Cámara: 12MP
¿Disponible?: Sí
