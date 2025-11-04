"""
Examen: Gestión de Inventario con Persistencia JSON y Programación Orientada a Objetos
Autor/a: Jaime Luna del Valle
Fecha: 4/11/2025

Objetivo:
Desarrollar una aplicación orientada a objetos que gestione un inventario de productos
con persistencia de datos en ficheros JSON y uso de listas y diccionarios anidados.

Clases requeridas:
- Proveedor
- Producto
- Inventario

"""

import json
import os


# ======================================================
# Clase Proveedor
# ======================================================

class Proveedor:
    def __init__(self, nombre, contacto,codigo):
        self.nombre = nombre
        self.contacto = contacto
        self.codigo = codigo


    def __str__(self):

        return f"nombre proveedor: {self.nombre}, contacto: {self.contacto}"


# ======================================================
# Clase Producto
# ======================================================

class Producto:
    def __init__(self, codigo, nombre, precio, stock, proveedor):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.proveedor = proveedor


    def precio_stock(self):
        return self.precio * self.stock


    def __str__(self):

        return f"[{self.codigo}] {self.nombre} - {self.precio_stock()} ({self.stock}) | Proveedor: {self.proveedor.nombre} ({self.proveedor.contacto}))"
        # TODO: devolver una representación legible del producto
        # Ejemplo: "[P001] Teclado - 45.99 € (10 uds.) | Proveedor: TechZone (ventas@techzone.com)"


# ======================================================
# Clase Inventario
# ======================================================

class Inventario:
    def __init__(self, nombre_fichero = "inventario.json"):
        self.nombre_fichero = nombre_fichero
        self.producto = []

    def cargar(self):

        try:
            
            with open(self.nombre_fichero, 'r') as f:
                lista_temporal = json.load(f)
        
            for p in lista_temporal:
                print(p)
                nuevoProducto = Producto(p["codigo"],p["nombre"],p["precio"],p["stock"],proveedor = 
                                Proveedor(p["proveedor"]["codigo"],p["proveedor"]["nombre"],p["proveedor"]["contacto"]))
                

                self.producto.append(nuevoProducto)

        except (json.JSONDecodeError, FileNotFoundError):
            print("El fichero no se ha  encontrado o está vacio")
            self.producto = []

    def guardar(self):

        try:
            with open(self.nombre_fichero, 'w', encoding="utf-8") as f:
                json.dump([produc.__dict__ for produc in self.producto],f,indent=4, default=str)
        except (json.JSONDecodeError, FileNotFoundError):
            print("El fichero no se ha  encontrado o está vacio")


    def anadir_producto(self, producto):


        for listpro in self.producto:
            if listpro.codigo == producto.codigo:
                print("El codigo ya existe")
                break

        else: self.producto.append(producto)

        print(producto)
    def mostrar(self):
        
        for pro in self.producto:
            print(pro)

    def buscar(self, codigo):


        for producto in self.producto:
            if producto.codigo == codigo:
                return producto
            
        else: return None
        """
        Devuelve el producto con el código indicado, o None si no existe.
        """
        # TODO: buscar un producto por código


    def modificar(self, codigo, nombre=None, precio=None, stock=None):

        for p in self.producto:
            if p.codigo == codigo:
                p.nombre = nombre
                p.precio = precio
                p.stock = stock
            

    def eliminar(self, codigo):
        """
        Elimina un producto del inventario según su código.
        """
        # TODO: eliminar el producto de la lista
        pass

    def valor_total(self):
        """
        Calcula y devuelve el valor total del inventario (precio * stock).
        """
        # TODO: devolver la suma total del valor del stock
        pass

    def mostrar_por_proveedor(self, nombre_proveedor):
        """
        Muestra todos los productos de un proveedor determinado.
        Si no existen productos de ese proveedor, mostrar un mensaje.
        """
        # TODO: filtrar y mostrar los productos de un proveedor concreto
        pass


# ======================================================
# Función principal (menú de la aplicación)
# ======================================================

def main():
    inventario = Inventario()
    inventario.cargar()

    # TODO: crear el objeto Inventario y llamar a los métodos según la opción elegida
    while True:
        print("\n=== GESTIÓN DE INVENTARIO ===")
        print("1. Añadir producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Modificar producto")
        print("5. Eliminar producto")
        print("6. Calcular valor total")
        print("7. Mostrar productos de un proveedor")
        print("8. Guardar y salir")

        opcion = input("Seleccione una opción: ")


        if opcion == '1':
            print("Apartado producto \n")

            codigop = input("Inserte un codigo de producto recuerde que debe ser unico: ")
            nombre = input("Inserte el nombre del producto: ")
            precio = float(input("Inserte el precio del producto: "))
            stock = int(input("Inserte el stock de dicho producto: "))
            
            print("Apartado proveedor \n")

            codigopro = input("Inserte el codigo del proveedor: ")
            nproveedor = input("Inserte el nombre del proveedor: ")
            contacto = input("Inserte el contacto del proveedor: ")
            
            if inventario.buscar(codigop) == None:
                produc = Producto(codigop,nombre,precio,stock,proveedor = Proveedor(codigopro,nproveedor,contacto))
                inventario.anadir_producto(produc)
                print("Se inserto el producto")
            else: print("El codigo del producto ya existe")


        if opcion == '2':
            print("El inventario contiene: ")
            inventario.mostrar()

        if opcion == '3':
            codigo = input("Inserte el codigo del producto que desea buscar: ")

            prodct = inventario.buscar(codigo)

            prodct.__str__()
            
        if opcion == '4':
            print("Vamos a modificar un producto\n")
            codigo = input("Inserte el codigo del producto que desea actualizar: ")

            if inventario.buscar(codigo) == None:
                print("El codigo no es el adecuado o no existe ese producto")

            else:
                pr = inventario.buscar(codigo)
                print("Recuerde si pulsa enter se queda como está\n")
                nuevo_nombre = input("Inserte el nuevo nombre: ")
                nuevo_stock = int(input("Inserte el nuevo stock: "))
                nuevo_precio = input("Inserte el nuevo precio: ")

                print(pr)

                inventario.modificar(codigo,nuevo_nombre or pr.nombre,
                                      float(nuevo_precio) or pr.precio,
                                      nuevo_stock or pr.stock)



        if opcion == '5':
            pass
        if opcion == '6':
            pass
        if opcion == '7':
            pass
        if opcion == '8':
            inventario.guardar()
            print ("Cerrando menu")
            break


if __name__ == "__main__":
    main()
